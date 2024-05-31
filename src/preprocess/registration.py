import os
import numpy as np
import matplotlib.pyplot as plt
import ants
from ants.utils.convert_nibabel import to_nibabel
import nibabel as nib


def rigid_reg(fixed: str, moving: str, save_path: str):
    ants_fixed = ants.image_read(fixed)
    ants_moving = ants.image_read(moving)

    res = ants.registration(
        fixed=ants_fixed, moving=ants_moving, type_of_transform="Rigid"
    )

    transform = ants.read_transform(res["fwdtransforms"][0])

    ants_warped = ants.apply_ants_transform(
        transform, ants_moving, data_type="image", reference=ants_fixed
    )

    nib.save(ants_warped, os.path.join(save_path, 'MRI_warped.nii.gz'))
    nib.save(ants_fixed, os.path.join(save_path, 'CT_fixed.nii.gz'))

    return ants_warped


def apply_manual_shift(image: ants.ANTsImage, manual_shift=(0, 0, 5)):
    """
    Apply a manual shift to an image.

    Args:
        image: ants.ANTsImage, the image to be shifted.
        manual_shift: tuple, the manual shift to be applied in the (x, y, z) directions.

    Returns:
        ants.ANTsImage: the shifted image.
    """
    # Convert manual shift to a transformation matrix
    manual_shift_transform = ants.create_ants_transform(
        dimension=image.dimension,
        transform_type="Euler3DTransform",
        translation=manual_shift
    )

    # Apply the manual shift to the image
    shifted_image = ants.apply_ants_transform(
        transform=manual_shift_transform,
        moving=image,
        data_type="image"
    )

    return shifted_image
