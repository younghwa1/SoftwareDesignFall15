import numpy as np
import cv2


cap = cv2.VideoCapture('DW_forecast.mp4')
kernel = np.ones((21, 21), 'uint8')

while(cap.isOpened()):
    ret, frame = cap.read()
    face_cascade = cv2.CascadeClassifier('/home/kim/Desktop/haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    for (x, y, w, h) in faces:
        frame[y:y+h, x:x+w, :] = cv2.dilate(frame[y:y+h, x:x+w, :], kernel)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255))
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()