import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

# We are using OpenCV to achieve object detection from live frame
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
first_read = True

font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (10, 20) 
org_2 = (10, 70) 

# fontScale 
fontScale = 0.9
   
# Blue color in BGR 
color = (0, 0, 0) 
color_2 = (0,0,255)
  
# Line thickness of 2 px 
thickness = 2
   
cap = cv2.VideoCapture(0)


def monitor_human():
    return_var = 0

    ret, img = cap.read()

    while(ret):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 5, 1, 1)
        eyes = []
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(50, 50))
        if(len(faces) > 0):
            for (x, y, w, h) in faces:
                img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 10)

                roi_face = gray[y:y+h, x:x+w]
                roi_face_clr = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(
                    img, 1.3, 5, minSize=(20, 20))

                for (ex, ey, ew, eh) in eyes:
                

                    image = cv2.circle(img, (int(ex+ew/2), int(ey + eh/2)), radius = ew//2, color = (0, 0, 255), thickness = 2)


        status = "Faces: " + str(len(faces)) + "  Eyes: " + str(len(eyes))

        if len(faces) !=0 and len(eyes) != 0:

            presence = "Student attending class"
            img = cv2.putText(img, presence , org_2, font,  
                        fontScale, color, thickness, cv2.LINE_AA) 

        else:
            presence = "Student distracted :("
            img = cv2.putText(img, presence , org_2, font,  
                        fontScale, color_2, thickness, cv2.LINE_AA) 

        img = cv2.putText(img, status , org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 

        

        return img


while(True):
    try:
        im = monitor_human()

        cv2.imshow("student-sight",im)
        if cv2.waitKey(1) == 27: 
            cv2.destroyAllWindows()

            break  # esc to quit
    except KeyboardInterrupt:
        print("end")
        cv2.destroyAllWindows()
        break
