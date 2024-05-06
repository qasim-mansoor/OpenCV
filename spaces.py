import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

# Colour Spaces

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# BGR to HSV (Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)

#BGR to Lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("Lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow("RGB", rgb)
# plt.imshow(rgb)
# plt.show()

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSVBGR", hsv_bgr)

cv.waitKey(0)