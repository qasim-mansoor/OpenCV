import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# Paint the image a certain color
# blank[:] = 0, 255,0
# cv.imshow('Green', blank)

# blank[:] = 0,0,255
# cv.imshow('Red', blank)

# Paint a specific area a certain colour
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Red Box', blank)

# # Drawing a rectange
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
# cv.rectangle(blank, (250,0), (500,500), (255,0,0), thickness=-1)
# cv.imshow('Rectangle', blank)

# # Drawing a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), radius=40, color=(0,0,255),thickness=-1)
# cv.imshow('Circle', blank)

# Drawing a line
# cv.line(blank, (0,0), (250,500), (0,255,0), thickness=1)
# cv.imshow('Line', blank)

#Writing text on an Image
cv.putText(blank, 'Hello, my name is 0', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow("Text", blank)

cv.waitKey(0)