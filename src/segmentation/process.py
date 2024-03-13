from __future__ import print_function
import os
import math
import json
import pickle

import numpy as np
import skimage as ski
import nibabel as nib
import cv2

INTERPOLATION_COEF = 2 ** 3


def slice_img_generator(input_file, interpolation=False):
    """

    """
    if interpolation:
        interpol_coeff = INTERPOLATION_COEF
    else:
        interpol_coeff = 1

    try:
        img = nib.load(input_file)
    except nib.filebasedimages.ImageFileError:
        print("Error: Unable to load the .nii file.")
        return
    img_data = img.get_fdata()
    for i in range(img_data.shape[2]):
        slice_data = img_data[:, :, i].copy()
        yield cv2.resize(slice_data, (0,0), fx=interpol_coeff, fy=interpol_coeff)


def perform_thresholding(img_gen, is_mri=False, interpolation=False):
    """
    Perform thresholding
    """
    if interpolation:
        interpol_coeff = INTERPOLATION_COEF
    else:
        interpol_coeff = 1

    # FIXME geometrical model of phantom or autodetect!!!!
    phantom_radius = 144
    img = next(img_gen)
    if is_mri:
        img = ski.util.invert(img)
    mask = np.zeros_like(img)
    img_shape = img.shape
    mask = cv2.circle(mask, (img_shape[0]//2, img_shape[1]//2), phantom_radius * interpol_coeff, (255, 255, 255), -1)
    image = cv2.bitwise_and(img, mask)
    ret, thresh1 = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
    yield thresh1.astype(np.uint8)


def isolate_markers(threshold_gen, save_path, interpolation=False):
    """
    Isolate markers
    """
    if interpolation:
        # TODO discover what values are suitable for interpol_mult (find rule)
        min_area = 650
        max_area = 1150
    else:
        min_area = 5
        max_area = 50

    marker_coords = []
    for threshold_img in threshold_gen:
        image = np.array(threshold_img, dtype=np.uint8)

        # Filter out large non-connecting objects
        cnts = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            area = cv2.contourArea(c)
            if area < min_area:
                cv2.drawContours(image, [c], 0, 0.5, -1)

        # Morph open using elliptical shaped kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
        opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=3)

        result_image = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)
        slice_coords = []

        cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            area = cv2.contourArea(c)
            if min_area < area < max_area:
                ((x, y), r) = cv2.minEnclosingCircle(c)
                cv2.circle(result_image, (int(x), int(y)), 0, (255, 255, 255), 1)
                slice_coords.append(
                    (np.round(int(x) / INTERPOLATION_COEF, 3), np.round(int(y) / INTERPOLATION_COEF, 3)))
        while len(slice_coords) < 88:
            slice_coords.append((100, 100))
        while len(slice_coords) > 88:
            slice_coords.pop()
        marker_coords.append(slice_coords)

    # FIXME i dont want to save it into pickle dump
    with open(os.path.join(save_path), 'wb') as f:
        pickle.dump(marker_coords, f, pickle.HIGHEST_PROTOCOL)


def count_difference(ct_path, mri_path, save_path):
    """
    Counts differences
    """
    # Ensure the output directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    with open(ct_path, 'rb') as f:
        coords_ct = pickle.load(f)
    with open(mri_path, 'rb') as f:
        coords_mri = pickle.load(f)

    distances = []
    slice_distances = {}

    for slice_num in range(len(coords_ct)):
        slice_distances[f'{slice_num}'] = {}
        slice_distances[f'{slice_num}']['distances'] = []
        for point_ct in coords_ct[slice_num]:
            for point_mri in coords_mri[slice_num]:
                distance = math.sqrt((point_ct[0] - point_mri[0]) ** 2 + (point_ct[1] - point_mri[1]) ** 2)
                if distance < 5 * INTERPOLATION_COEF:
                    slice_distances[f'{slice_num}']['distances'].append(distance)
                    distances.append(distance)

    for key in slice_distances.keys():
        distances_array = np.array(slice_distances[key]['distances'])
        if len(distances_array) > 0:
            slice_distances[key]['Mean difference, mm'] = float(np.mean(distances_array))
            non_zero = distances_array[np.nonzero(distances_array)]
            if len(non_zero) > 0:
                slice_distances[key]['Min difference, mm'] = float(np.min(distances_array[np.nonzero(distances_array)]))
            else:
                slice_distances[key]['Min difference, mm'] = float(0)
            slice_distances[key]['Max difference, mm'] = float(np.max(distances_array))
            slice_distances[key]['Std, mm'] = float(np.std(distances_array))
            slice_distances[key]['Number of differences > 0.5 mm'] = int((distances_array > 0.5).sum())
            slice_distances[key]['Number of differences > 1 mm'] = int((distances_array > 1).sum())
        else:
            slice_distances[key]['Mean difference, mm'] = float(0)
            slice_distances[key]['Min difference, mm'] = float(0)
            slice_distances[key]['Max difference, mm'] = float(0)
            slice_distances[key]['Std, mm'] = float(0)
            slice_distances[key]['Number of differences > 0.5 mm'] = int(0)
            slice_distances[key]['Number of differences > 1 mm'] = int(0)

    distances = np.array(distances)
    mean_distance = np.mean(distances)
    non_zero = distances[np.nonzero(distances)]
    if len(non_zero) > 0:
        min_distance = np.min(distances[np.nonzero(distances)])
    else:
        min_distance = float(0)
    max_distance = np.max(distances)
    std_distance = np.std(distances)
    num_05 = (distances > 0.5).sum()
    num_1 = (distances > 1).sum()

    params = {'Mean difference, mm': np.round(float(mean_distance), 2),
              'Min difference, mm': np.round(float(min_distance), 2),
              'Max difference, mm': np.round(float(max_distance), 2),
              'Std, mm': np.round(float(std_distance), 2),
              'Number of differences > 0.5 mm': int(num_05),
              'Number of differences > 1 mm': int(num_1)}

    with open(os.path.join(save_path, 'difference_stats.json'), 'w') as fp:
        json.dump(params, fp)
    with open(os.path.join(save_path, 'slice_difference_stats.json'), 'w') as fp:
        json.dump(slice_distances, fp)
    return params, distances, slice_distances


def get_coords(markers_path):
    """
    Get coordinates of markers
    """
    with open(markers_path, 'rb') as f:
        coords_array = np.array(pickle.load(f))

    shape_coords = coords_array.shape
    list_of_points = []
    for z_slice in range(shape_coords[0]):
        for num_of_point in range(shape_coords[1]):
            list_of_points.append([coords_array[z_slice, num_of_point, 0], coords_array[z_slice, num_of_point, 1], z_slice])
    return list_of_points


