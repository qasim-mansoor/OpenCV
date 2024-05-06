import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)

threshold_inv, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inverse", thresh_inv)

# Adaptive thresholding - Auto threshold value

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive thresholding", adaptive_thresh)

cv.waitKey(0)