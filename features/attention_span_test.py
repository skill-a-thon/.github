import cv2
import time
pip install opencv-contrib-python
#numpy for array related functions
import numpy as np
#dlib for deep learning modules and face landmark detection
import dlib 
#face_utils foe basic operations of conversion
from imutils import face_utils
#initialising the cam and taking the instance
cap = cv2.VideoCapture(0)
import winsound

#initialising the face and landmark detector
detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#status marking for the current state
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)


def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist


def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    #is driver blinking?
    # NOTE: change the values according to our system later, trial and error
    if ratio > 0.25:  #opened eye
        return 2
    elif (ratio > 0.21 and ratio <= 0.25):  #droopy eye
        return 1
    else:  #closed eye
        return 0

e=0
s=0
while True:  # 2 or 1
    _, frame = cap.read()  # returns ret variable and camera frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # changes BGR to RGB (openCV read in BGR)

    faces = detector(gray)
    #detected face in faces array
    for face in faces:  #frontal face detector rectangle that is formed
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)  #(frame, region of interest)
        landmarks = face_utils.shape_to_np(
            landmarks)  #shaping dlib result in numpy array

        #eye landmarks (redcued by 1 bc array index)

        left_blink = blinked(landmarks[36], landmarks[37], landmarks[38],
                             landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43], landmarks[44],
                              landmarks[47], landmarks[46], landmarks[45])

        #state of the person is judged below
        n=1
        if(left_blink==0 or right_blink==0):
          sleep+=1
          drowsy=0
          active=0
          if(sleep==2):
            status="Attention span test completed"
            winsound.PlaySound("alarmbeep.wav",winsound.SND_ASYNC)
            color = (255,0,0)
            e=time.time()
            break
                   

        elif (left_blink == 1 or right_blink == 1):
            sleep = 0
            active = 0
            drowsy += 1
            if (drowsy > 6):
                status = "Your attention is lowering"
                color = (0, 0, 255)

        else:
            drowsy = 0
            sleep = 0
            active += 1
            if(active==1):
                status = "Attention span test begins"
                s=time.time()
            if (active > 3):
                status = "You are currently attentive"
                color = (0, 255, 0)

        cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                    color, 3)

        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Frame", frame)
    #cv2.imshow("Result of detector", face_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

print("Measured attention span is: ",s-e)
