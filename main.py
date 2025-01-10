import cv2
import numpy as np
import mediapipe as mp
import face_recognition
import time

def FrameRate(pastTime):
    """This function is to get the framerate of the video"""
    cTime = time.time()
    fps = 1/(cTime-pastTime)
    return fps, cTime

vid = vid = cv2.VideoCapture(0)
frame_width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

pTime = 0

mpFaceDetection = mp.solutions.face_detection #grabing the face class from the import
mpdraw = mp.solutions.drawing_utils #giving the ablility to draw on each frame of the video
FaceDetection = mpFaceDetection.FaceDetection(0.75)#the parameters is the confidances lvl which it needs to detect it the original is .5

while True:
    success, frame = vid.read()
    vidS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = FaceDetection.process(vidS)
    if results.detections:
        for id,detection in enumerate(results.detections):
            """
            print(detection.score)#the confidnces score
            print(detection.location_data.relative_bounding_box)#the coordinates  of the face
            mpdraw.draw_detection(frame,detection) #makes landmarks of the face and makes a box
            """
            boundingBox = detection.location_data.relative_bounding_box 
            ih, iw, ic = frame.shape
            SampleboundingBox = int(boundingBox.xmin * iw), int(boundingBox.ymin * ih), int(boundingBox.width * iw), int(boundingBox.height * ih)

            cv2.rectangle(frame,SampleboundingBox, (255, 0,255), 2)
    fps, pTime = FrameRate(pTime)
    cv2.putText(frame, f'fps: {int(fps)}', (0,30), cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,0), 2)
    #cv2.putText(input vide, text,position, font, scale of the font, color of the text, thinkness )
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) == ord("q"):#waits until the key is pressed
        break