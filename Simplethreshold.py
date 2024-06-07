import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command
image = cv2.imread('gl.jpg')

# to convert the image in grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold = 160
# cv2.THRESH_BINARY: If  the pixel intensity is greater than the threshold, the pixel value is set to 255(white), else it is set to 0 (black).
ret, thresh1 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

# cv2.THRESH_BINARY_INV: Inverted or Opposite case of cv2.THRESH_BINARY.If  the pixel intensity is greater than the threshold, the pixel value is set to 0(black), else it is set to 255 (white).
ret, thresh2 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)

# cv.THRESH_TRUNC: If  the pixel intensity is greater than the threshold,the pixel values are set to be the same as the threshold. All other values remain the same
ret, thresh3 = cv2.threshold(img, threshold, 255, cv2.THRESH_TRUNC)

#cv.THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.All other pixel values remain same
ret, thresh4 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO)

#cv.THRESH_TOZERO_INV: Inverted or Opposite case of cv2.THRESH_TOZERO.
ret, thresh5 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO_INV)

# the window showing output images
# with the corresponding thresholding
# techniques applied to the input images
cv2.imshow('Original', image)
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Zero Threshold', thresh4)
cv2.imshow('Zero Inverted', thresh5)

# De-allocate any associated memory usage
cv2.waitKey(0)
cv2.destroyAllWindows()