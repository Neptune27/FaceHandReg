import os
import pickle
import sys

import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage, Qt


class FacialRegThread(QThread):
    updateFrame: Signal = Signal(QImage)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.trained_file = None
        self.status = True
        self.cap = True
        print("Loading Face Detector...")
        self.protoPath = "FaceRecognition/face_detection_model/deploy.prototxt"
        self.modelPath = "FaceRecognition/face_detection_model/res10_300x300_ssd_iter_140000.caffemodel"
        self.detector = cv2.dnn.readNetFromCaffe(self.protoPath, self.modelPath)

        # load serialized face embedding model
        print("Loading Face Recognizer...")
        self.embedder = cv2.dnn.readNetFromTorch("FaceRecognition/openface_nn4.small2.v1.t7")

        # load the actual face recognition model along with the label encoder
        self.le = pickle.loads(open("FaceRecognition/output/le.pickle", "rb").read())
        self.isTraining = False
        self.personName = "WTF"

    def run(self):
        self.recognizer = pickle.loads(open("FaceRecognition/output/recognizer.pickle", "rb").read())
        if self.isTraining:
            self.training()
        else:
            self.running()

    def running(self):
        self.cap = cv2.VideoCapture(0)
        while self.status:
            ret, frame = self.cap.read()

            if not ret:
                continue

            imageBlob = cv2.dnn.blobFromImage(
                cv2.resize(frame, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)

            # apply OpenCV's deep learning-based face detector to localize faces in the input image
            self.detector.setInput(imageBlob)
            detections = self.detector.forward()
            h, w, ch = frame.shape

            # loop over the detections
            for i in range(0, detections.shape[2]):
                # extract the confidence (i.e., probability) associated with the prediction
                confidence = detections[0, 0, i, 2]

                # filter out weak detections
                if confidence > 0.7:
                    # compute the (x, y)-coordinates of the bounding box for the face
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # extract the face ROI
                    face = frame[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]

                    # ensure the face width and height are sufficiently large
                    if fW < 20 or fH < 20:
                        continue

                    # construct a blob for the face ROI,
                    # then pass the blob through our face embedding model to obtain the 128-d quantification of the face
                    faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                                     (96, 96), (0, 0, 0), swapRB=True, crop=False)
                    self.embedder.setInput(faceBlob)
                    vec = self.embedder.forward()

                    # perform classification to recognize the face
                    preds = self.recognizer.predict_proba(vec)[0]
                    j = np.argmax(preds)
                    proba = preds[j]
                    name = self.le.classes_[j]

                    # draw the bounding box of the face along with the associated probability
                    text = "{}: {:.2f}%".format(name, proba * 100)
                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.rectangle(frame, (startX, startY), (endX, endY),
                                  (0, 0, 255), 2)
                    cv2.putText(frame, text, (startX, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

            # # Reading the image in RGB to display it
            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #
            # # Creating and scaling QImage
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

            # Emit signal
            self.updateFrame.emit(scaled_img)
        sys.exit(-1)

    def training(self):
        self.cap = cv2.VideoCapture(0)
        path = f"./FaceRecognition/dataset/{self.personName}"
        print("Training")
        try:
            os.mkdir(path)
        except Exception as ex:
            print(ex)

        total = 0
        totalFrame = 0
        while self.status:
            ret, frame = self.cap.read()

            if not ret:
                continue

            imageBlob = cv2.dnn.blobFromImage(
                cv2.resize(frame, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)

            # apply OpenCV's deep learning-based face detector to localize faces in the input image
            self.detector.setInput(imageBlob)
            detections = self.detector.forward()
            h, w, ch = frame.shape

            # loop over the detections
            for i in range(0, detections.shape[2]):
                # extract the confidence (i.e., probability) associated with the prediction
                confidence = detections[0, 0, i, 2]

                # filter out weak detections
                if confidence > 0.5:
                    # compute the (x, y)-coordinates of the bounding box for the face
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # extract the face ROI
                    face = frame[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]

                    # ensure the face width and height are sufficiently large
                    if fW < 20 or fH < 20:
                        continue

                    # construct a blob for the face ROI,
                    # then pass the blob through our face embedding model to obtain the 128-d quantification of the face
                    faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                                     (96, 96), (0, 0, 0), swapRB=True, crop=False)
                    self.embedder.setInput(faceBlob)
                    vec = self.embedder.forward()

                    # perform classification to recognize the face
                    preds = self.recognizer.predict_proba(vec)[0]
                    j = np.argmax(preds)
                    proba = preds[j]
                    name = self.le.classes_[j]

                    # draw the bounding box of the face along with the associated probability
                    text = "{}: {:.2f}% {}".format(name, proba * 100, total)
                    #
                    totalFrame += 1
                    if totalFrame % 5 == 0:
                        try:
                            cv2.imwrite(f"{path}/{total}{self.personName}.jpg", frame)
                            total += 1
                            if total > 200:
                                self.cap.release()
                                cv2.destroyAllWindows()
                                self.status = False
                        except Exception:
                            print("OK!")
                        pass

                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.rectangle(frame, (startX, startY), (endX, endY),
                                  (0, 0, 255), 2)
                    cv2.putText(frame, text, (startX, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

            # cascade = cv2.CascadeClassifier(self.trained_file)
            # ret, frame = self.cap.read()
            # if not ret:
            #     continue
            #
            # # Reading frame in gray scale to process the pattern
            # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #
            # detections = cascade.detectMultiScale(gray_frame, scaleFactor=1.1,
            #                                       minNeighbors=5, minSize=(30, 30))
            #
            # # Drawing green rectangle around the pattern
            # for (x, y, w, h) in detections:
            #     pos_ori = (x, y)
            #     pos_end = (x + w, y + h)
            #     color = (0, 255, 0)
            #     cv2.rectangle(frame, pos_ori, pos_end, color, 2)
            #
            # # Reading the image in RGB to display it
            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #
            # # Creating and scaling QImage
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

            # Emit signal
            self.updateFrame.emit(scaled_img)
        sys.exit(-1)
