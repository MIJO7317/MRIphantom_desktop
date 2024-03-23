Getting Started
=====

Welcome to the MRIphantom Getting Started page. This page contains instructions that you should follow
to start using the application.

System requirements
--------------------
MRIphantom is compatible with modern operating systems such as Windows, MacOS, and Linux. However, it may encounter compatibility issues on older machines, particularly those running Windows 8.1 or earlier.

Operating system versions
__________________________

Windows: Windows 10 or 11.

macOS: macOS Big Sur (11) or later (compatible with both Apple Silicon and Intel-based computers).

Linux: any recent LTS distribution, for example, Ubuntu 18.04 and later.

Hardware configuration
________________________

Memory: At least 4GB of RAM.

Display: A minimum resolution of 1024 x 768 (FullHD is recommended).

Graphics: Dedicated GPU memory is not required, but recommended for faster rendering.

IO-devices: Compatible with any standard mouse and keyboard.

Internet connection: Not required at the moment.

Installation from source
--------------------------

To use MRIphantom, first clone the repository to your local machine:

.. code-block:: console

   $ git clone git@gitlab.com:bzavolovich/MRIphantom_desktop.git

Make sure you have the latest Python version installed.

Create a virtual environment in the project directory by running
the following command:

.. code-block:: console

    $ python -m venv venv

and activate it (Linux, macOS):

.. code-block:: console

    $ source venv/scripts/activate

or (Windows):

.. code-block:: console

    ./venv/Scripts/Activate.ps1

Install necessary packages using requirements.txt:

.. code-block:: console

    $ pip install -r requirements.txt

Run the application by executing the following command:

.. code-block:: console

    $ python app.py


Using MRIphantom QA Solution
-------------------------------

MRIphantom is currently in its early stages of development, offering a straightforward yet promising set of features.
While it may not be as complex, navigating through its functionalities can still be confusing.
Here's how you can get started with MRIphantom QA Solution:

Basics
_____________________

The software consists of one main window from which you can start analyzing MRI images, and output section allowing you to navigate between various visualization in a simple manner.
All you need to start using the program is CT and MRI images of Elekta MRI phantom.
Currently, our solution is compatible with pre-registered images saved in .nii.gz (or .nii) formats.
We are working on implementing DICOM support soon.

To conduct the analysis, simply click on the 'Calculate' button.

Refer to the documentation or README files for instructions on using the software.
