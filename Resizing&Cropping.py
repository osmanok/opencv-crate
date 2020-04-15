import cv2
import numpy as np

img = cv2.imread('Resources/mercedes.png')
print(img.shape)

imgResize = cv2.resize(img, (300,200))

cv2.imshow("Image", imgResize)

cv2.waitKey(0)
