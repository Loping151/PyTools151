# --------------------------------------------------------------------------------
# Author: Loping151
# GitHub: https://github.com/Loping151/pytools151
# Description: This repository contains a collection of Python tools designed to
#              enhance productivity and simplify various tasks. The code is open
#              for use and can be freely used, modified, and distributed.
# License: MIT License - Feel free to use and modify the code as you wish.
# --------------------------------------------------------------------------------
import cv2
import os
import numpy as np
    

def crop_image(image_path, crop_values, save_path=None):
    """
    Crops an image based on the provided top, bottom, left, and right values using OpenCV.
    
    Args:
        image_path (str): Path to the image file.
        crop_values (list): A list containing the top, bottom, left, and right values for cropping.
        
    Returns:
        numpy.ndarray: The cropped image as a numpy array.
    """
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Ensure the image was loaded
    if image is None:
        raise FileNotFoundError(f"No such file: {image_path}")
    
    # Image dimensions are accessed in height, width format
    height, width = image.shape[:2]
    
    # Calculate new dimensions for cropping
    top, bottom, left, right = crop_values
    cropped_image = image[top:height-bottom, left:width-right]
    
    if save_path is not None:
        cv2.imwrite(save_path, cropped_image)
    
    return cropped_image