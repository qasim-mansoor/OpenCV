import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow("Average Blur", average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian Blur", gauss)

# Median Blur
med = cv.medianBlur(img, 3)
cv.imshow("Median Blur", med)

# Bilateral Blur
bil = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bil)

cv.waitKey(0)

