import cv2
import matplotlib.pyplot as plt
img = cv2.imread('img.jpg')
original_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.axis("off")
plt.imshow(original_img)
plt.axis("off")
watercolour_image = cv2.stylization(original_img, sigma_s=100, sigma_r=0.45)
plt.imshow(watercolour_image)
cv2.imwrite('sketch1.png',watercolour_image)
True
