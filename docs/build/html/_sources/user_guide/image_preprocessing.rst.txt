Image Preprocessing
===================

Two main methods of image preprocessing are available.

You can either work with images in their original resolution for quick results,
or choose preprocessing with interpolation to improve the quality of marker detection.
We select the scale factor by which we upscale initial images.
This enables the marker detection algorithm to operate at a higher quality, resulting in improved precision and finer outcomes.

Pipeline of image processing can be divided into several steps:

1. Begin by unpacking input scans slice by slice.
2. Select the upscale factor (=1 in case of original resolution and =2**3 for interpolation).
3. Upscale images according to the selected factor (or leave as is).
4. Apply masking to isolate the central portion of the phantom, containing the plastic rods.
5. Employ thresholding segmentation to eliminate all except the rods.
6. Execute marker detection.
7. Export the marker coordinates as .pickle files.
8. Conduct analysis using the saved data.

You can also look at the examples below.

Original resolution
----------------------

**TODO pictures**

Interpolation (better quality detection)
-----------------------------------------

**TODO pictures**
