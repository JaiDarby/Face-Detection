
# Creating database
# It captures images and stores them in datasets 
# folder under the folder name of sub_data

import cv2, sys, numpy, os

haar_file = 'haarcascade_frontalface_default.xml' #Haar file
 
datasets = 'datasets' #All faces in database can be found here


sub_data = 'Trey' #Creates sub folder for each name (Make sure to enter new name)  
 

path = os.path.join(datasets, sub_data) #Creates the new dataset

#Checks if sub_data already exists
if not os.path.isdir(path):

    os.mkdir(path)
 
# defining the size of images 
(width, height) = (130, 100)    

face_cascade = cv2.CascadeClassifier(haar_file) #Says to use haar file for recognition

webcam = cv2.VideoCapture(0) #opens web cam
 
# The program loops until it has 30 images of the face.
count = 1
while count < 30: 

    (_, im) = webcam.read() #Takes screenshot

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #Makes pictrues gray

    faces = face_cascade.detectMultiScale(gray, 1.3, 4) #Detects face in picture

    for (x, y, w, h) in faces:

        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face = gray[y:y + h, x:x + w]

        face_resize = cv2.resize(face, (width, height))

        cv2.imwrite('% s/% s.png' % (path, count), face_resize)

    count += 1

     

    cv2.imshow('OpenCV', im)

    key = cv2.waitKey(10)

    if key == 32:

        break
