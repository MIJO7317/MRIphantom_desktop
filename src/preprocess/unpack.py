"""
Module: unpack
Module for unpacking DICOM files
"""
from subprocess import check_call
import os
from pathlib import Path
import dicom2nifti
import dicom2nifti.settings as settings

def unpack_dicoms(source_folder: Path, target_folder: Path, name=None):
    settings.disable_validate_orthogonal()
    settings.enable_resampling()
    dicom2nifti.dicom_series_to_nifti(
        source_folder,
        os.path.join(target_folder, name),
        reorient_nifti=True
    )
