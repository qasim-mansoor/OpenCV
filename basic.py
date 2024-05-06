import cv2 as cv

# Some important functions

img = cv.imread('Photos/lady.jpg')
cv.imshow('Cat', img)

# Converting an image to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# Edge Cascade - Edges can be decresed by applying a blur
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# Dilating an image using canny edges
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow("Resized", resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)