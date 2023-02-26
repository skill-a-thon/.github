
import cv2
import numpy as np
#We are using OpenCV to achieve object detection from live frame
from django.conf import settings
import requests
import os
url = 'https://raw.githubusercontent.com/sanjay-thiyagarajan/projects/master/haarcascade_frontalface_default.xml'
r = requests.get(url, allow_redirects=True)
open('haarcascade_frontalface_default.xml', 'wb').write(r.content)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
cap =  cv2.VideoCapture(-1)

def look_for_human(fcap = cap , face_cascade = face_cascade):

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray,5,1,1)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(50,50))
     
    if len(faces)!= 0:
        return True
    else:
        return False


