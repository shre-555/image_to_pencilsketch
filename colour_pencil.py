import cv2
import numpy as np

def colour_sketch(img):
    edge=cv2.edgePreservingFilter(img,sigma_s=200,sigma_r=0.85, flags=1)
    f2= cv2.divide(img, edge, scale=256)
    f3=cv2.convertScaleAbs(f2, alpha=1.27, beta=-70)
     
          
    # Apply gamma correction. 
    gamma_corrected = np.array(255*(f3 / 255) ** 1.8, dtype = 'uint8')  
    return gamma_corrected
