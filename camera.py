import numpy as np
import cv2 as cv
import time
cap = cv.VideoCapture(0)
flag=1
count=1
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    string=str(count)+".png"
    cv.imwrite("1.png",frame)
    count+=1
    time.sleep(2)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()