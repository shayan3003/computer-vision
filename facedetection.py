import cv2 as cv
import sys

# Get user supplied values
imagePath = sys.argv[0]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv.CascadeClassifier(cascPath)

# Read the image
image = cv.imread(imagePath)


# Detect faces in the image
faces = faceCascade.detectMultiScale(

    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv.cv.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow("Faces found", image)
cv.waitKey(0)