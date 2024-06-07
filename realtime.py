import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while (1):
    ret,frame = cap.read()
    cv2.imshow("Original",frame)
    edges = cv2.Canny(frame, 100, 200,True)
    cv2.imshow('Edges',edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        cap.release()
        cv2.destroyAllwindows()


