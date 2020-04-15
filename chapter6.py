import cv2
import numpy as np

img = cv2.imread('Resources/Lenna.png')

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow("hor", imgHor)
cv2.imshow('ver', imgVer)

cv2.waitKey(0)