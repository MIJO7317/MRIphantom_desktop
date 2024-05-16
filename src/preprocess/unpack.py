"""
Module: unpack
Module for unpacking DICOM files
"""
from subprocess import check_call
from pathlib import Path


def unpack_dicoms(source_folder: Path, target_folder: Path, name=None):
    """Converts folder of dicoms into a nii.gz file."""
    cmd = ['dcm2niix', '-z', 'y']
    if name is not None:
        cmd.append('-f')
        cmd.append(name)
    cmd.append('-o')
    cmd.append(f'{str(target_folder)}/')
    cmd.append(f'{str(source_folder)}/')
    return check_call(cmd)


