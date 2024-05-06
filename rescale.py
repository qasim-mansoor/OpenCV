import cv2 as cv

def changeRes(width, height):
    # Live Videos only
    capture.set(3, width)
    capture.set(4,height)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.2)
    cv.imshow('Video Resized', frame_resized)
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()