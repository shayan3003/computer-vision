import cv2
import numpy as np

from realtime import cap

capture =cv2.VideoCapture(0)

while(True):

    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break


capture.release()
cv2.destroAllWindows()
