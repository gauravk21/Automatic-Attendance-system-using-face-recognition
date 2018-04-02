from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import imutils
import os

faceCascade = cv2.CascadeClassifier('haarcascade_frontal_default.xml')

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 10

rawCapture=PiRGBArray(camera,size=(640,480))
time.sleep(0.1)
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,480))
count = 0

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image=frame.array
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    count+=1
    if(count > 120):
        break
    out.write(image)
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        break
    
    
#camera.release()
out.release()
cv2.destroyAllWindows()
    