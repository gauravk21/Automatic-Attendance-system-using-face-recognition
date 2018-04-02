from picamera.array import PiRGBArray
from picamera  import PiCamera
import time
import cv2
import imutils
import os

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = PiCamera()
camera.resolution = (320,240)
camera.framerate =  10

rawCapture = PiRGBArray(camera,size=(320,240))
#recognizer = cv2.createLBPHFaceRecognizer()
time.sleep(0.1)
out=cv2.VideoWriter('training_data/outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (320,240))
count = 0

for frame in  camera.capture_continuous(rawCapture, format="bgr", use_video_port= True):
        image = frame.array
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        count +=1
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.05,
            minNeighbors = 5,
            minSize = (30,30),
            flags = cv2.CASCADE_SCALE_IMAGE
            )
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imwrite('training_data/'+ str(count)+ '.jpg',gray)
            timestamp = time.time()
            resized_image = cv2.resize(gray[y:y+h ,x:x+w], (164, 164)) 
            #cv2.imwrite('training_data/'+ str(timestamp) + '.jpg',gray[y:y+h ,x:x+w])
            cv2.imwrite('training_data/'+ str(timestamp) + '.jpg',resized_image)
        
        if count > 120:
            break
        
        out.write(image)
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if key == ord("q"):
            break


out.release()
cv2.destroyAllWindows()
