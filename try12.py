#!/usr/bin/python

# Import the required modules
import cv2, os
import numpy as np
from PIL import Image

# For face detection we will use the Haar Cascade provided by OpenCV.
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = './query_data_set'

# For face recognition we will the the LBPH Face Recognizer 
recognizer = cv2.face.createEigenFaceRecognizer(threshold=80.0)
recognizer.load('datamatrix.yml')


    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
#image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.sad')]
    # images will contains face images
#images = []
    # labels will contains the label that is assigned to the image
#labels = []
#for image_path in image_paths:
        # Read the image and convert to grayscale
image_pil = Image.open('query_data_set/outpy.19.jpg').convert('L')
#gray = cv2.cvtColor(image_pil,cv2.COLOR_BGR2GRAY)
    #new_image = cv2.resize(image_pil,(164,164))
        # Convert the image format into numpy array
image = np.array(image_pil, 'uint8')
#print(image.shape)
        # Get the label of the image
    #nbr = int(os.path.split(image_path)[1].split(".")[0].replace("s", ""))
##        nbr = int(os.path.split(image_path)[-1].split(".")[1])
        # Detect the face in the image
faces = faceCascade.detectMultiScale(image,
        scaleFactor = 1.05,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
        )
        #If face is detected, append the face to images and the label to labels
       
for (x, y, w, h) in faces:
    
    #result = cv2.face.MinDistancePredictCollector()
    recognizer.predict(image)
    #Id = result.getLabel()
    #print(Id)
    #conf= result.getDist()/100
    #print(conf)
    id = 1  
    #print(recognizer.predict(image))
    if(id == 1):
                print(" chanchal is present")
    else:
                print("chanchal is absent")


            

       



##Append the images with the extension .sad into image_paths
#image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sad')]
#for image_path in image_paths:
   #predict_image_pil = Image.open(image_path).convert('L')
   #predict_image = np.array(predict_image_pil, 'uint8')
   #aces = faceCascade.detectMultiScale(predict_image)
        #for (x, y, w, h) in faces:
            #collector = cv2.face.StandardCollector_create((cv2.resize(predict_image[y: y + h, x: x + w],(164,164))))
        #recognizer.predict_collect()
##        nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
        #nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("s", ""))
        #
        #if nbr_actual == nbr_predicted:
           # print ("{} is Correctly Recognized with confidence {}".format(nbr_actual, conf))
        #else:
            #print ("{} is Incorrect Recognized as {}".format(nbr_actual, nbr_predicted))
        #cv2.waitKey(1000)

