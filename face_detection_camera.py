import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('/users/shreykhandelwal/opencv/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
	ret, frame= cap.read()
	frame = cv2.resize(frame, None, fx= 0.5, fy= 0.5, interpolation= cv2.INTER_AREA)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in face_rects:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255, 0), 3)
	cv2.imshow('face detector', frame)

	c = cv2.waitKey(0)
	if c==27:
		break

cap.release()
cv2.destroyAllWindows()
