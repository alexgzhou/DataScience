# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:43:48 2018

@author: thinkPad
"""
import numpy as np
import cv2
import os
import imutils
from imutils import face_utils
import dlib

#split video by frame
for i in range(1,33):
    for j in range(1,41):
        
cap = cv2.VideoCapture('s01_trial01.avi')

try:
    if not os.path.exists('avi2jpg'):
        os.makedirs('avi2jpg')
except OSError:
    print ('Error: Creating directory of data')

c = 1
timeF = 2
while(True):
    ret, frame = cap.read()# Capture frame-by-frame
    if(c%timeF == 0): #每隔timeF帧进行存储操作
        row, col = frame.shape[:2]  
        frame = frame[：, 100:col, :] # 如果图片太大，从中心位置取600×600的切片
        frame = imutils.resize(frame, width=600)
        cv2.imwrite('./avi2jpg/frame%d.jpg' % (c/2),frame)
    c += 1
    if not ret: 
        break

cap.release() 
cv2.destroyAllWindows()  # destroy all the opened windows

# initialize dlib's face detector (HOG-based) and then create the facial landmark predictor
PREDICTOR_PATH = 'shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)

landmark = []
for i in range(1,10):
    # load the input image, resize it, and convert it to grayscale
    name = './avi2jpg/frame' + str(i) + '.jpg'
    image = cv2.imread(name)
    #image = imutils.resize(image, width=600)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale image
    rects = detector(gray, 1)
    # determine the facial landmarks for the face region, then convert the facial landmark (x, y)-coordinates to a NumPy array
    shape = predictor(gray, rects[0])
    shape = face_utils.shape_to_np(shape)
    landmark.append(shape)
        
#    # show the output image with the face detections + facial landmarks
#    cv2.imshow("Output", image)
#    cv2.waitKey(0)

np.savez("landmark.npz", landmark) 

