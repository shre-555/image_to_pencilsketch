import cv2
import numpy as np

def sketch(img):
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    b1=cv2.GaussianBlur(gray,(45,45),0)
    f= cv2.divide(gray, b1, scale=256)
    return f
