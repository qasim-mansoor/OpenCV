import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# canny = cv.Canny(blur, 125, 175) # Find edges
# # cv.imshow("Edges", canny)
# cv.imshow("Blur", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)


contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours Drawn", blank)

print(len(contours))

cv.waitKey(0)