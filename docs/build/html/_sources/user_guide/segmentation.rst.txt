Image Segmentation
======================

Image segmentation is a crucial step in image processing pipeline.

Currently, only a single method of image segmentation is in the software, but it's the simplest and quickest option available.
It doesn't require a dedicated GPU since it's not a neural network-based approach.

Thresholding
--------------

Threshold segmentation is a technique used to separate plastic rods from the background based on pixel intensity values.

A threshold value is chosen (different for both modalities), and pixels in the image whose intensity values are above or below this threshold are classified as belonging to the region of interest or background, respectively.
This method is straightforward and effective for images with clear intensity differences between objects and background regions (our case).

Rods on CT scans have values [170, 255].
Rods on MRI scans have values [215, 255].

**TODO insert pictures (examples)**

Neural Network
------------------

**TODO**

