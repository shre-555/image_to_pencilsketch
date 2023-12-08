import cv2
import numpy
def texturedpencil(img):
    f1,f2=cv2.pencilSketch(img, sigma_s=10, sigma_r=0.40, shade_factor=0.02)
    return f2