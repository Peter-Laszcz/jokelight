from __future__ import print_function
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sid_obj = SentimentIntensityAnalyzer()
import cv2
import os
import subprocess
import cv2 as cv
from mss import mss
from PIL import Image
import numpy as np
import argparse
from ultralytics import YOLO

#whisper_installation="python -m pip install git+https://github.com/openai/whisper.git"
#os.system(whisper_installation)

model = YOLO("best.pt")

def detectAndDisplay(screen,name):

    screen_gray = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
    screen_gray = cv.equalizeHist(screen_gray)
    faces = face_cascade.detectMultiScale(screen_gray)
    if any(map(len, faces)):
        largest_face = max(faces, key=lambda f: f[2] * f[3])
        x, y, w, h = largest_face
        frame = screen.copy()
        dim = min(w,h)
        frame = frame[y:y + dim, x:x + dim]
        if dim != 48:
            if dim < 48:
                frame = cv.resize(frame, (48, 48), interpolation=cv.INTER_LINEAR)
            else:
                frame = cv.resize(frame, (48, 48), interpolation=cv.INTER_AREA)

        frame = cv.resize(frame, (48, 48), interpolation=cv.INTER_LINEAR)
        print (name)
        results = model(frame)
        r = results[0]
        class_names = r.names
        for b in r.boxes:
            print(f"Class name: {class_names[b.cls]}")
        cv.imwrite(framename, frame)
face_cascade_name = "C:\\Users\\onegr\\PycharmProjects\\PythonProject\\.venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml"#args.face_cascade
eyes_cascade_name = "C:\\Users\\onegr\\PycharmProjects\\PythonProject\\.venv\\Lib\\site-packages\\cv2\\data\\haarcascade_eye_tree_eyeglasses.xml"#args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
for vid in os.listdir('videos'):
    vidmp3 = (vid[:-4])+'.mp3'
    mp3_conversion_command = 'ffmpeg -y -i '+os.path.join('videos', vid)+' -vn -acodec mp3 '+os.path.join('audios',vidmp3)
    os.system(mp3_conversion_command)
    speech_recognition_command = "python -m whisper "+os.path.join('audios',vidmp3)+" --model medium"
    os.system(speech_recognition_command)
    cam = cv2.VideoCapture(os.path.join('videos',vid))
    fps = cam.get(cv2.CAP_PROP_FPS)
    vidtsv=(vid[:-4])+'.tsv'
    with open(vidtsv) as f:
        next(f)
        counter = 0
        for line in f:
            (start, end, text) = line.strip().split("\t")
            sentiment_dict = sid_obj.polarity_scores(text)
            if sentiment_dict['compound'] > 0:
                tag = "/pos"
            elif sentiment_dict['compound'] < 0:
                tag = "/neg"
            else:
                tag = "/neu"
            print(text + "(" + tag + ")")
            framems = (int(end)-int(start))//6
            for framecount in range(0,6):
                cam.set(cv2.CAP_PROP_POS_MSEC, int(start)+((framems)*framecount))
                success, image = cam.read()
                framename = (str(counter)+ str(framecount) + ".jpg")
                detectAndDisplay(image,framename)
            counter += 1