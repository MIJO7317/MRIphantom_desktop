from __future__ import print_function
import os
import math
import json
import pickle

import numpy as np
from PIL import Image
import skimage as ski
from skimage import io
import skimage.transform as trans
from skimage import img_as_ubyte
import cv2


def perform_thresholding(test_path, save_path, target_size=(512, 512), is_mri=False, as_gray=True, ):
    """
    Perform thresholding
    """
    for f in sorted(os.listdir(test_path)):
        img = io.imread(os.path.join(test_path, f), as_gray=as_gray)
        img = trans.resize(img, target_size)

        # Ensure the output directory exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        if is_mri:
            img = ski.util.invert(img)

        img = img_as_ubyte(img)

        mask = np.zeros_like(img)
        mask = cv2.circle(mask, (258, 255), 144, (255, 255, 255), -1)
        image = cv2.bitwise_and(img, mask)

        ret, thresh1 = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

        # image = cv2.circle(img*255, (258, 258), 146, (255, 0, 0), 1)

        im = Image.fromarray((thresh1).astype(np.uint8))
        im.save(os.path.join(save_path, f))


def isolate_markers(image_path, save_path):
    """
    Isolate markers
    """
    # Ensure the output directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

        # select only .png files
    file_list = [file for file in sorted(os.listdir(image_path), key=lambda x: int(x.split('.')[0])) if
                 file.endswith('.png')]

    marker_coords = []
    for image_filename in file_list:
        file_path = os.path.join(image_path, image_filename)
        pre = cv2.imread(file_path)
        image = cv2.cvtColor(pre, cv2.COLOR_BGR2GRAY)

        # Filter out large non-connecting objects
        cnts = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            area = cv2.contourArea(c)
            if area < 5:
                cv2.drawContours(image, [c], 0, 0.5, -1)

        # Morph open using elliptical shaped kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
        opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=3)

        blank_image = np.zeros((512, 512, 3), np.uint8)

        slice_coords = []

        cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            area = cv2.contourArea(c)
            if area > 5 and area < 50:
                ((x, y), r) = cv2.minEnclosingCircle(c)
                cv2.circle(blank_image, (int(x), int(y)), 0, (255, 255, 255), 1)
                slice_coords.append((int(x), int(y)))
        while len(slice_coords) < 88:
            slice_coords.append((100, 100))

        while len(slice_coords) > 88:
            slice_coords.pop()

        marker_coords.append(slice_coords)

        # save image as png
        cv2.imwrite(os.path.join(save_path, image_filename), blank_image)

    with open(os.path.join(save_path, 'data.pickle'), 'wb') as f:
        pickle.dump(marker_coords, f, pickle.HIGHEST_PROTOCOL)


def count_difference(ct_path, mri_path, save_path):
    """
    Counts differences
    """
    # Ensure the output directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    with open(os.path.join(ct_path, 'data.pickle'), 'rb') as f:
        coords_ct = pickle.load(f)

    with open(os.path.join(mri_path, 'data.pickle'), 'rb') as f:
        coords_mri = pickle.load(f)

    # all values together
    distances = []
    # not together, but per slice
    slice_distances = {}

    for slice_num in range(len(coords_ct)):
        slice_distances[f'{slice_num}'] = {}
        slice_distances[f'{slice_num}']['distances'] = []
        for point_ct in coords_ct[slice_num]:
            for point_mri in coords_mri[slice_num]:
                distance = math.sqrt((point_ct[0] - point_mri[0]) ** 2 + (point_ct[1] - point_mri[1]) ** 2)
                if distance < 5:
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
    min_distance = np.min(distances[np.nonzero(distances)])
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


def get_coords_ct(ct_path):
    """
    Get coordinates of CT markers
    """
    with open(os.path.join(ct_path, 'data.pickle'), 'rb') as f:
        coords_ct = np.array(pickle.load(f))

    shape_coords = coords_ct.shape
    list_of_points = []
    for z_slice in range(shape_coords[0]):
        for num_of_point in range(shape_coords[1]):
            list_of_points.append([coords_ct[z_slice, num_of_point, 0], coords_ct[z_slice, num_of_point, 1], z_slice])
    return list_of_points


def get_coords_mri(mri_path):
    """
    Get coordinates of MRI markers
    """
    with open(os.path.join(mri_path, 'data.pickle'), 'rb') as f:
        coords_mri = np.array(pickle.load(f))

    shape_coords = coords_mri.shape
    list_of_points = []
    for z_slice in range(shape_coords[0]):
        for num_of_point in range(shape_coords[1]):
            list_of_points.append([coords_mri[z_slice, num_of_point, 0], coords_mri[z_slice, num_of_point, 1], z_slice])
    return list_of_points
