#!/usr/bin/python

# Import the required modules
import cv2, os
import numpy as np
from PIL import Image

# For face detection we will use the Haar Cascade provided by OpenCV.
# For face recognition we will the the LBPH Face Recognizer 

def get_images_and_labels(path):
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)


    path = './training_set'
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        nbr = int(os.path.split(image_path)[-1].split(".")[0])
        print (nbr)
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
            images.append(cv2.resize(image[y: y + h, x: x + w],(164,164)))
            ##nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", cv2.resize(image[y: y + h, x: x + w],(164,164)))
            cv2.waitKey(50)
            
    # return the images list and labels list
    return images, labels

# Path to the Yale Dataset

# Call the get_images_and_labels function and get the face images and the 
# corresponding labels



# Perform the tranining)
def train():
            path = './training_set'
            images, labels = get_images_and_labels(path)
            cv2.destroyAllWindows()
            recognizer = cv2.face.createEigenFaceRecognizer()
            recognizer.train(images, np.array(labels))
            print ("training completed")
            recognizer.save('datamatrix.yml')
            print (" Training is success")
            
            
            
train()     
#recognizer.load('datamatrix.yml')

#nbr_predicted, confidence = recognizer.predict()
#print("confindece is meet")                                               
                                               
                                               
