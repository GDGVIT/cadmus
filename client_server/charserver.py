# importing necessary libs
import numpy as np
import cv2
from fastai.vision import *
import sys
import socketio
import os

# standard Python
sio = socketio.Client()
sio.connect("https://cadmus-server.herokuapp.com/")

if len(sys.argv) > 1:
    sio.emit("join", {"room": sys.argv[1]})

path = os.getcwd()
imgpath = os.path.join(path, "pred-image.jpg")

# configuring the webcam
cap = cv2.VideoCapture(2)
"""
if you have an additional external webcam, the above statement will become cv2.VideoCapture(3)
"""
cap.set(3, 640)
cap.set(4, 480)

# setting the font
font = cv2.FONT_HERSHEY_SIMPLEX

# setting the learner object
learn = load_learner(path)

# prediction of each frames
def predict():
    img = open_image(imgpath)
    pred_class, pred_idx, outputs = learn.predict(img)
    return pred_class


def webcam_stream():
    fps = 0
    prediction = ""
    title = "Cadmus"
    while True:
        # capturing frames from video stream
        ret, frame = cap.read()

        if fps == 30:  # can be adjusted based on user's signing speed.
            image = frame[50:300, 50:300]
            cv2.imwrite("pred-image.jpg", image)
            pred = predict()
            temp = str(pred)
            if temp == "space":
                prediction += "  "
            elif temp == "del":
                prediction = prediction[:-1]
            elif temp == "nothing":
                prediction += ""
            else:
                prediction += temp
            fps = 0

        fps += 1

        # displaying title
        cv2.putText(frame, title, (180, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # displaying prediction
        cv2.putText(
            frame, prediction, (50, 400), font, 2, (255, 255, 255), 2, cv2.LINE_AA
        )

        # outlining the ROI
        cv2.rectangle(frame, (50, 50), (300, 300), (250, 0, 0), 2)
        cv2.imshow("Cadmus ", frame)

        sio.emit("word", prediction)
        prediction = ""
        # exit when q is pressed
        key = cv2.waitKey(1)
        if key == ord("q"):
            break


if __name__ == "__main__":
    webcam_stream()

cap.release()
cv2.destroyWindow("cadmus")
