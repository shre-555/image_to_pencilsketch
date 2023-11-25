import cv2
import numpy as np

def colour_sketch(img):
    edge=cv2.edgePreservingFilter(img,sigma_s=180,sigma_r=0.5)
    f2= cv2.divide(img, edge, scale=256)
    return f2
