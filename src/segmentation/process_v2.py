import cv2
import numpy as np
import math
from scipy.spatial import cKDTree
import pickle
import json
import os
from joblib import Parallel, delayed

def round_to_nearest_odd(number):
    """
    Round a given number to the nearest odd integer.

    Parameters:
    number (float): The number to be rounded.

    Returns:
    int: The nearest odd integer to the given number. If the number is equidistant
         between two odd integers, it rounds up if the number is positive and down if negative.
    """
    return int(number) | 1


def find_main_circle(image, standard_image_size=512, standard_kernel_size=41, low_search_part=0.25,
                     high_search_part=0.75):
    """
    Detect the main circle in the given image using the Hough Circle Transform.

    Parameters:
    - image: Input image in which to detect the circle.
    - standard_image_size: Standard size to which the image is resized for processing if it is smaller.
    - standard_kernel_size: Optimal kernel size for standart size image to remove all unnecessary details using median blurring.
    - low_search_part: Lower bound for the radius search range as a fraction of the radius of the inscribed circle in the image's bounding box.
    - high_search_part: Upper bound for the radius search range as a fraction of the radius of the inscribed circle in the image's bounding box.

    Returns:
    - circles[0]: The detected circle parameters (x, y, radius) if found, otherwise None.
    """

    # Determine the minimum dimension of the image
    image_size = min(image.shape[:2])

    # Define scale factor
    scale_factor = standard_image_size / image_size if image_size < standard_image_size else 1.0

    # Resize the image if necessary
    if scale_factor != 1.0:
        image = cv2.resize(image, (0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    # Calculate the kernel size for median blurring
    kernel_size = round_to_nearest_odd(standard_kernel_size * image_size / standard_image_size)

    # Apply median blur to the image
    blurred_image = cv2.medianBlur(image, kernel_size)

    otsu, _ = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    otsu = max(1, otsu)

    # Perform Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(
        blurred_image,
        cv2.HOUGH_GRADIENT,
        dp=1, # The inverse ratio of the accumulator resolution to the image resolution. A value of 1 means the accumulator has the same resolution as the input image.
        minDist=max(image_size, standard_image_size), # Minimum distance between the centers of the detected circles. This is set to the size of the image to avoid detecting multiple nearby circles.
        param1=otsu, # Higher threshold for the Canny edge detector. A lower value is chosen to detect more edges.
        param2=1, # Accumulator threshold for the circle centers at the detection stage. A lower value means more circles will be detected.
        minRadius=int(low_search_part * image_size / 2),  # <-┐
        maxRadius=int(high_search_part * image_size / 2)  # <-┴ These values were chosen because the desired circle is presumably within this size range.
    )

    # Check if any circles were found
    if circles is not None and scale_factor != 1.0:
        circles[0][0][:3] /= scale_factor

    # Return the detected circle parameters
    return circles[0][0] if circles is not None else None, blurred_image

def estimate_h_gradient(image, scale_factor=1.3):
        """Estimation of h based on the analysis of image gradients."""
    
        # Calculating gradients in x and y
        grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
        
        # Calculating the magnitude of the gradient
        grad_mag = np.sqrt(grad_x**2 + grad_y**2)
        
        # Estimation of h based on the average magnitude of the gradient
        return np.clip(np.mean(grad_mag)*scale_factor, 3, 100)


def get_points(image, circle, blured, relative_wall_thickness=0.05, circles_ratio=0.1):
    """
    Extracts points from the given image within a specified circular region.

    This function performs the following steps:
    1. Denoises the image using Fast Non-Local Means Denoising.
    2. Creates a mask with a circular region of interest.
    3. Applies the mask to the denoised image.
    4. Normalizes the pixel values within the masked region.
    5. Thresholds the image using Otsu's method to create a binary image.
    6. Removes all pixels outside the mask.
    7. Creates a secondary mask to define a wall thickness around the circle.
    8. Uses flood fill to remove unwanted regions within the binary image.
    9. Finds contours in the binary image.
    10. Extracts the center points of the contours.

    Parameters:
    image (numpy.ndarray): The input image from which points are to be extracted.
    circle (tuple): A tuple containing the (x, y) coordinates and radius of the circle.
    relative_wall_thickness (float, optional): The diameter of the thinnest rod as a fraction of the phantom's radius. Default is 0.05.
    circles_ratio (float, optional): The ratio of the inner circle radius to the outer circle radius. Default is 0.1.

    Returns:
    list: A list of (x, y) coordinates representing the center points of the detected contours.
    """

    # Create a mask with a circular region of interest
    mask = np.zeros_like(image)
    cv2.circle(mask, (round(circle[0]), round(circle[1])), round(circle[2]*(1 - relative_wall_thickness)), 255, -1)
    cv2.circle(mask, (round(circle[0]), round(circle[1])), round(circles_ratio * circle[2]), 0, -1)

    blured_mean = int(np.mean(blured[mask == 255]))

    # Make illumination correction
    result = image.astype(np.int16) - blured.astype(np.int16) + blured_mean

    # Rounding negative values to 0 and limiting the maximum to 255
    correction_image = np.clip(result, 0, 255).astype(np.uint8)

    # Normalize the pixel values within the masked region
    normalized_image = cv2.normalize(correction_image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U, mask)
    
    # Denoise the image using Fast Non-Local Means Denoising
    denoise_image = cv2.fastNlMeansDenoising(normalized_image, h=estimate_h_gradient(normalized_image))
    
    # Create mask for find Otsu's threshold
    otsu_mask = np.zeros_like(denoise_image)
    cv2.circle(otsu_mask, (round(circle[0]), round(circle[1])), round(circle[2]), 255, -1)
    otsu_loc = np.where(otsu_mask == 255)
    
    # Find Otsu's threshold
    otsu, _ = cv2.threshold(denoise_image[otsu_loc], 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    binary_image = np.full(image.shape, 255, dtype=np.uint8)

    # Threshold the image using Otsu's method to create a binary image
    binary_image[otsu_loc] = cv2.threshold(denoise_image[otsu_loc], otsu, 255, cv2.THRESH_BINARY_INV)[1][:,0]

    mask2 = np.zeros_like(image)
    cv2.circle(mask2, (round(circle[0]), round(circle[1])), round(circle[2]*(1 - 1.25 * relative_wall_thickness)), 255, -1)
    cv2.circle(mask2, (round(circle[0]), round(circle[1])), round(circle[2]*(circles_ratio  + relative_wall_thickness)), 0, -1)

    # Set everything outside the mask to black
    binary_image[mask2 == 0] = 0

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Extract the center points of the contours and return points
    return [(cX, cY, width * height) for contour in contours for (cX, cY), (width, height), _ in [cv2.minAreaRect(contour)]]

def process_slice(mri_image, ct_image, config, voxel_size):
    size_for_resizing = config['segmentation']['size_for_resizing']
    relative_wall_thickness = config['segmentation']['relative_wall_thickness']
    circles_ratio = config['segmentation']['circles_ratio']
    low_search_part = config['segmentation']['low_search_part']
    high_search_part = config['segmentation']['high_search_part']
    num_points = config['segmentation']['num_points']

    # Calculate scaling factors for resizing images
    scale_mri_factor = size_for_resizing / min(mri_image.shape[:2])
    scale_ct_factor = size_for_resizing / min(ct_image.shape[:2])

    # Resize MRI and CT images to the specified size
    mri_image = cv2.resize(mri_image, (size_for_resizing, size_for_resizing), interpolation=cv2.INTER_CUBIC)
    ct_image = cv2.resize(ct_image, (size_for_resizing, size_for_resizing), interpolation=cv2.INTER_CUBIC)

    # Detect the main circle in the resized MRI and CT images
    mri_circle, blured_mri = find_main_circle(mri_image, low_search_part=low_search_part, high_search_part=high_search_part)
    ct_circle, blured_ct = find_main_circle(ct_image, low_search_part=low_search_part, high_search_part=high_search_part)

    # Extract points of interest from the MRI and CT images within the detected circles
    mri_points = get_points(mri_image, mri_circle, blured_mri, relative_wall_thickness=relative_wall_thickness, circles_ratio=circles_ratio)
    ct_points = get_points(255 - ct_image, ct_circle, 255 - blured_ct, relative_wall_thickness=relative_wall_thickness, circles_ratio=circles_ratio)

    def process_points(points, num_points):
        # Sort the points by area (S) in descending order
        sorted_points = sorted(points, key=lambda p: p[2], reverse=True)
        
        # Select the first num_points of pairs (x,y) or all if there are fewer num_points
        result = [(x, y) for x, y, _ in sorted_points[:num_points]]

        # If there are fewer points than num_points, fill in the array (NaN, NaN) and return them
        return result + [(math.nan, math.nan)]*(num_points - len(result))

    # Processing mri_points
    mri_points = process_points(mri_points, num_points)

    # Processing ct_points
    ct_points = process_points(ct_points, num_points)

    return np.array(mri_points) / scale_mri_factor * voxel_size, np.array(ct_points) / scale_ct_factor * voxel_size

def segmentation(phantom_type, mri_images, ct_images, mri_save_path, ct_save_path, voxel_size=1):
    config_paths = {
        "elekta_axial": 'assets/phantom_configs/elekta_axial.json',
        "phantom_1_axial": 'assets/phantom_configs/phantom_1_axial.json'
    }
    
    with open(config_paths[phantom_type], 'r') as f:
        config = json.load(f)

    if mri_images.shape[2] != ct_images.shape[2]:
        return 'Error: MRI and CT data have different number of images.'

    results = Parallel(n_jobs=-1)(delayed(process_slice)(mri_images[:, :, i], ct_images[:, :, i], config, voxel_size) for i in range(mri_images.shape[2]))

    all_mri_points, all_ct_points = zip(*results)
    with open(mri_save_path, "wb") as f:
        pickle.dump(all_mri_points, f, pickle.HIGHEST_PROTOCOL)
    with open(ct_save_path, "wb") as f:
        pickle.dump(all_ct_points, f, pickle.HIGHEST_PROTOCOL)

    return all_mri_points, all_ct_points


def count_difference_2(ct_path, mri_path, save_path, interpolation_coef=1.0, distance_threshold=3.0):
    """
    Counts differences between CT and MRI markers using nearest neighbor search and saves statistics.
    """

    # Ensure the output directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Load CT and MRI coordinates from pickle files with dtype=object to handle inhomogeneous data
    with open(ct_path, "rb") as f:
        coords_ct = np.array(pickle.load(f), dtype=object)
    with open(mri_path, "rb") as f:
        coords_mri = np.array(pickle.load(f), dtype=object)

    # Initialize lists to store distances and per-slice statistics
    distances = []
    slice_distances = {}

    # Process each slice and calculate distances using KD-tree for nearest neighbor search
    for slice_num, (ct_slice, mri_slice) in enumerate(zip(coords_ct, coords_mri)):
        slice_distances[slice_num] = {"distances": []}

        ct_points = [point for point in ct_slice if not (math.isnan(point[0]) or math.isnan(point[1]))]
        mri_points = [point for point in mri_slice if not (math.isnan(point[0]) or math.isnan(point[1]))]

        # Convert to numpy arrays for KDTree
        ct_points = np.array(ct_points)
        mri_points = np.array(mri_points)

        tree = cKDTree(ct_points)
        slice_distances[slice_num]["distances"], indices = tree.query(mri_points)

        # Filter and store distances below the threshold
        for distance in slice_distances[slice_num]["distances"]:
            if distance <= distance_threshold:
                distances.append(distance)

    # Convert distances to numpy array and filter them
    distances = np.array(distances)
    filtered_distances = distances[distances <= distance_threshold]

    # Convert slice_distances distances to lists for JSON serialization
    for key in slice_distances:
        slice_distances[key]["distances"] = slice_distances[key]["distances"].tolist()

    # Calculate per-slice statistics
    for key in slice_distances:
        distances_array = np.array(slice_distances[key]["distances"])
        distances_array = distances_array[distances_array <= distance_threshold]

        if len(distances_array) > 0:
            slice_distances[key]["Mean difference, mm"] = np.mean(distances_array)
            non_zero = distances_array[distances_array > 0]
            slice_distances[key]["Min difference, mm"] = np.min(non_zero) if len(non_zero) > 0 else 0
            slice_distances[key]["Max difference, mm"] = np.max(distances_array)
            slice_distances[key]["Std, mm"] = np.std(distances_array)
            slice_distances[key]["Percentage of differences > 0.5 mm"] = (distances_array > 0.5).sum() / len(distances_array) * 100
            slice_distances[key]["Percentage of differences > 1 mm"] = (distances_array > 1).sum() / len(distances_array) * 100
        else:
            slice_distances[key].update({
                "Mean difference, mm": 0,
                "Min difference, mm": 0,
                "Max difference, mm": 0,
                "Std, mm": 0,
                "Percentage of differences > 0.5 mm": 0,
                "Percentage of differences > 1 mm": 0,
            })

    # Calculate overall statistics
    if len(filtered_distances) > 0:
        mean_distance = np.mean(filtered_distances)
        non_zero = filtered_distances[filtered_distances > 0]
        min_distance = np.min(non_zero) if len(non_zero) > 0 else 0
        max_distance = np.max(filtered_distances)
        std_distance = np.std(filtered_distances)
        percentage_05 = (filtered_distances > 0.5).sum() / len(filtered_distances) * 100
        percentage_1 = (filtered_distances > 1).sum() / len(filtered_distances) * 100
    else:
        mean_distance = min_distance = max_distance = std_distance = percentage_05 = percentage_1 = 0

    params = {
        "Mean difference, mm": round(mean_distance, 2),
        "Min difference, mm": round(min_distance, 2),
        "Max difference, mm": round(max_distance, 2),
        "Std, mm": round(std_distance, 2),
        "Percentage of differences > 0.5 mm": round(percentage_05, 2),
        "Percentage of differences > 1 mm": round(percentage_1, 2),
    }

    # Save the statistics as JSON files
    with open(os.path.join(save_path, "difference_stats.json"), "w") as fp:
        json.dump(params, fp)
    with open(os.path.join(save_path, "slice_difference_stats.json"), "w") as fp:
        json.dump(slice_distances, fp)

    return params, distances, slice_distances
