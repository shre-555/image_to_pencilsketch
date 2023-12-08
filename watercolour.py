import cv2
import numpy as np

def oil_sketch(img, d=9, sigmaColor=75, sigmaSpace=75, brightness_factor=0.7, contrast_factor=1.3):
    watercolor_image = cv2.bilateralFilter(img, d=d, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)
    watercolor_image = cv2.convertScaleAbs(watercolor_image, alpha=contrast_factor, beta=brightness_factor)
    return watercolor_image
