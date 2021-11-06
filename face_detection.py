import cv2
img = cv2.imread('test.png')

face_cascade = cv2.CascadeClassifier('/users/shreykhandelwal/desktop/haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.waitKey()
