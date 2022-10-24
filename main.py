import cv2 as cv
import numpy as np

cap = cv.VideoCapture("video/sample.mp4")
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Cant receive frame!!!")
        break
    
    cv.imshow('frame', frame)
    if cv.waitKey(30) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

