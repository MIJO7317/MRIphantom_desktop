import numpy as np
from subprocess import check_call
from pathlib import Path
from pydicom import dcmread
from typing import Union
from dicom_csv.utils import Series
import os
import nibabel as nib
from PIL import Image

def dicom_to_nifti(source_folder: Path, target_folder: Path, name=None):
    """Converts folder of dicoms into a nii.gz file."""
    cmd = ['dcm2niix', '-z', 'y']
    if name is not None:
        cmd.append('-f')
        cmd.append(name)
    cmd.append('-o')
    cmd.append(f'{str(target_folder)}/')
    cmd.append(f'{str(source_folder)}/')
    return check_call(cmd)

def unpack_nii_stack(input_file, output_directory, output_format="PNG"):
    # Load the .nii file
    try:
        img = nib.load(input_file)
    except nib.filebasedimages.ImageFileError:
        print("Error: Unable to load the .nii file.")
        return
    
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Extract the 3D image data
    img_data = img.get_fdata()
    
    # Iterate through each slice and save as a 2D image
    for i in range(img_data.shape[2]):
        slice_data = img_data[:, :, i]
        slice_img = Image.fromarray((slice_data)).convert('RGB')

        # Generate the output filename
        output_filename = f"{i + 1}.{output_format.lower()}"
        output_path = os.path.join(output_directory, output_filename)

        # Save the slice as an image
        slice_img.save(output_path)
