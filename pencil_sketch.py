# import all the required modules
import numpy as np
import imageio
import scipy.ndimage
import cv2
import matplotlib.pyplot as plt 



# function to convert image into sketch
def rgb2gray(rgb):
	# 2 dimensional array to convert image to sketch
	return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])


def dodge(front, back):

	final_sketch = front*255/(255-back)
    #The multiplication by 255 and division by (255 - back) help scale the values to the 0-255 range
     # If the result is greater than 255, set it to 255
	final_sketch[final_sketch > 255] = 255
     # Set pixels to 255 where the background is already white (255)
	final_sketch[back == 255] = 255

	# Convert the result to 8-bit unsigned integer (uint8)
	return final_sketch.astype('uint8')


def pencil(img):
    gray = rgb2gray(img)

    i = 255-gray
    #Inverting the image helps to emphasize edges and details in the original image


    # to convert into a blur image, sigma is Standard deviation for Gaussian kernel
    blur = scipy.ndimage.filters.gaussian_filter(i, sigma=13)


    # calling the function
    r = dodge(blur, gray)

    return r



