import cv2
import numpy as np
import mediapipe as mp


capture =cv2.VideoCapture(0)

while(True):

    ret,frame = cap.read()
   

    cv2.imshow('frame',frame)
    cv2.waitkey(1)


capture.release()
cv2.destroAllWindows()
