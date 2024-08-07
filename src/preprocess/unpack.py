"""
Module: unpack
Module for unpacking DICOM files
"""
from subprocess import check_call
import os
from pathlib import Path
import dicom2nifti


def unpack_dicoms(source_folder: Path, target_folder: Path, name=None):
    dicom2nifti.dicom_series_to_nifti(
        source_folder,
        os.path.join(target_folder, name),
        reorient_nifti=True
    )
