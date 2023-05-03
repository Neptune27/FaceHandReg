import copy
import csv
import os
import pickle
import sys
from collections import deque

import cv2
import numpy as np
import mediapipe as mp
import pyautogui

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage, Qt

from HandsRecognition.app import *
from HandsRecognition.model.keypoint_classifier.keypoint_classifier import KeyPointClassifier
from Utils.Setting import Setting


class FacialRegThread(QThread):
    updateFrame: Signal = Signal(QImage)

    def __init__(self, parent=None, setting: Setting = None):

        QThread.__init__(self, parent)

        self.prevOpenApp = ""


        self.setting = setting


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

        self.use_static_image_mode = False
        self.min_detection_confidence = 0.7
        self.min_tracking_confidence = 0.5

        # Model load #############################################################
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.use_static_image_mode,
            max_num_hands=1,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence,
        )

        self.keypoint_classifier = KeyPointClassifier(model_path='HandsRecognition/model/keypoint_classifier'
                                                                 '/keypoint_classifier.tflite')

        # Read labels ###########################################################
        with open('HandsRecognition/model/keypoint_classifier/keypoint_classifier_label.csv',
                  encoding='utf-8-sig') as f:
            keypoint_classifier_labels = csv.reader(f)
            self.keypoint_classifier_labels = [
                row[0] for row in keypoint_classifier_labels
            ]

        self.use_brect = True

    def run(self):
        self.recognizer = pickle.loads(open("FaceRecognition/output/recognizer.pickle", "rb").read())
        if self.isTraining:
            self.training()
        else:
            self.running()

    def draw_info(self, frame, text, offset=0):
        # Black line
        cv.putText(frame, str(text), (10, 30 + offset), cv.FONT_HERSHEY_SIMPLEX,
                   1.0, (0, 0, 0), 4, cv.LINE_AA)

        # White text
        cv.putText(frame, str(text), (10, 30 + offset), cv.FONT_HERSHEY_SIMPLEX,
                   1.0, (255, 255, 255), 2, cv.LINE_AA)

    def running(self):
        # Coordinate history #################################################################
        history_length = 16

        #  ########################################################################
        mode = 0
        cvFpsCalc = CvFpsCalc(buffer_len=10)

        # Avg
        names = deque(maxlen=50)
        gestures = deque(maxlen=20)
        #

        self.cap = cv2.VideoCapture(0)
        while self.status:

            ret, frame = self.cap.read()

            fps = cvFpsCalc.get()

            if not ret:
                continue

            frame = cv.flip(frame, 1)

            frame.flags.writeable = False
            image = frame  # Mirror display

            imageBlob = cv2.dnn.blobFromImage(
                cv2.resize(frame, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)

            # apply OpenCV's deep learning-based face detector to localize faces in the input image
            self.detector.setInput(imageBlob)
            detections = self.detector.forward()
            h, w, ch = frame.shape

            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = self.hands.process(image)
            image.flags.writeable = True
            # print(results.multi_hand_landmarks)

            totalFace = 0
            name = "Unknown"
            hand_name = ""

            # loop over the detections
            for i in range(detections.shape[2]):
                # extract the confidence (i.e., probability) associated with the prediction
                confidence = detections[0, 0, i, 2]

                # filter out weak detections
                if confidence > 0.7:

                    totalFace += 1
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
                    if proba < 0.6:
                        continue
                    name = self.le.classes_[j]

                    # draw the bounding box of the face along with the associated probability
                    frame.flags.writeable = True
                    text = f"{name}: {proba * 100:.2f}%"
                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.rectangle(frame, (startX, startY), (endX, endY),
                                  (0, 0, 255), 2)
                    cv2.putText(frame, text, (startX, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                    frame.flags.writeable = False

            if totalFace != 1:
                self.draw_info(frame, f"{totalFace} face(s) != 1")

            else:
                ####################################################################
                if results.multi_hand_landmarks is not None:
                    for hand_landmarks, handedness in zip(results.multi_hand_landmarks,
                                                          results.multi_handedness):
                        frame.flags.writeable = False

                        # Bounding box calculation
                        brect = calc_bounding_rect(frame, hand_landmarks)
                        # Landmark calculation
                        landmark_list = calc_landmark_list(frame, hand_landmarks)

                        # Conversion to relative coordinates / normalized coordinates
                        pre_processed_landmark_list = pre_process_landmark(
                            landmark_list)

                        frame.flags.writeable = True

                        # Hand sign classification
                        hand_sign_id = self.keypoint_classifier(pre_processed_landmark_list)

                        hand_name = self.keypoint_classifier_labels[hand_sign_id]

                        # Drawing part
                        draw_bounding_rect_directly(self.use_brect, frame, brect)
                        draw_landmarks(frame, landmark_list)
                        draw_info_text(
                            frame,
                            brect,
                            handedness,
                            hand_name,
                        )

                names.append(name)
                gestures.append(hand_name)

                counterName = Counter(names)
                counterHand = Counter(gestures)

                self.draw_info(frame, f"{fps=}")
                self.draw_info(frame, f"MC: {counterHand.most_common(1)}, {counterName.most_common(1)}", 30)
                self.draw_info(frame, f"CC: {hand_name}: {counterHand[hand_name]}", 60)
                if hand_name == counterHand.most_common(1)[0][0]:
                    self.handle_input(name, hand_name, counterHand.most_common(1)[0][1])

            # # Reading the image in RGB to display it
            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #
            # # Creating and scaling QImage
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

            # Emit signal
            self.updateFrame.emit(scaled_img)
        sys.exit(-1)

    def handle_input(self, name, hand_name, mc):
        try:
            funcType: str = getattr(self.setting.user[name], hand_name)
            if funcType[0] == "L":
                pyautogui.moveRel(-5, 0, _pause=False)
            if funcType[0] == "R":
                pyautogui.moveRel(5, 0, _pause=False)
            if funcType[0] == "U":
                pyautogui.moveRel(0, -5, _pause=False)
            if funcType[0] == "D":
                pyautogui.moveRel(0, 5, _pause=False)
            if funcType[0] == "O":
                if mc == 20:
                    path = funcType.split(",")[1]
                    if self.prevOpenApp != path:
                        os.startfile(path)
                        self.prevOpenApp = path


        except AttributeError:
            pass
        except KeyError:
            pass

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

            frame = cv.flip(frame, 1)

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
                    text = f"{name}: {proba * 100:.2f}% {total}"
                    #
                    totalFrame += 1
                    if totalFrame % 2 == 0:
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
