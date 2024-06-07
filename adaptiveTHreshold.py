import cv2
import numpy as np

image= cv2.imread("lamp.jpg")

#convert into greyscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# adaptiveMethod − A variable of integer the type representing the adaptive method to be used. This will be either of the following two values:
ret, th1 = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)

# cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)

#cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Original', image)
cv2.imshow('Binary Threshold', th1)
cv2.imshow('Adaptive Threshold', th2)
cv2.imshow('Gaussain Adaptive Threshold', th3)

# De-allocate any associated memory usage
cv2.waitKey(0)
cv2.destroyAllWindows()

