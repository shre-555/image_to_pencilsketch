import cv2
import numpy
def texture(img):
    f1,f2=cv2.pencilSketch(img)
    return f2