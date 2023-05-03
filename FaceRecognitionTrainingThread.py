import os
import pickle

import cv2
import imutils
import numpy as np
from PySide6.QtCore import QThread, Signal
from imutils import paths
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC


class FaceRecognitionTrainingThread(QThread):
    updateLoadingBar: Signal = Signal()

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.protoPath = "FaceRecognition/face_detection_model/deploy.prototxt"
        self.modelPath = "FaceRecognition/face_detection_model/res10_300x300_ssd_iter_140000.caffemodel"
        self.detector = cv2.dnn.readNetFromCaffe(self.protoPath, self.modelPath)
        self.embedder = cv2.dnn.readNetFromTorch("FaceRecognition/openface_nn4.small2.v1.t7")

    def has_faces(self, names: list[str], path: str):
        for i in names:
            if i in path:
                return True
        else:
            return False

    def extractEmbedding(self):
        previousData = {"embeddings": [], "names": []}
        # initialize our lists of extracted facial embeddings and corresponding people names
        try:
            with open('FaceRecognition/output/embeddings.pickle', 'rb') as f:
                try:
                    previousData = pickle.load(f)
                except EOFError:
                    pass
        except FileNotFoundError:
            with open('FaceRecognition/output/embeddings.pickle', 'w') as f:
                pass
        knownEmbeddings = previousData["embeddings"]
        knownNames = previousData["names"]

        imagePaths = list(paths.list_images("FaceRecognition/dataset"))
        imagePaths = [path for path in imagePaths if not self.has_faces(knownNames, path)]
        print(imagePaths)
        # initialize the total number of faces processed

        # initialize the total number of faces processed
        total = 0

        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            print(f"Processing image {i}/{len(imagePaths)}")
            name = imagePath.split(os.path.sep)[-2]

            # load the image, resize it to have a width of 600 pixels (while maintaining the aspect ratio),
            # and then grab the image dimensions
            image = cv2.imread(imagePath)
            image = imutils.resize(image, width=600)
            (h, w) = image.shape[:2]

            # construct a blob from the image
            imageBlob = cv2.dnn.blobFromImage(
                cv2.resize(image, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)

            # apply OpenCV's deep learning-based face detector to localize faces in the input image
            self.detector.setInput(imageBlob)
            detections = self.detector.forward()

            # ensure at least one face was found
            if len(detections) > 0:
                # we're making the assumption that each image has only ONE face, so find the bounding box with the
                # largest probability
                i = np.argmax(detections[0, 0, :, 2])
                confidence = detections[0, 0, i, 2]

                # ensure that the detection with the largest probability also means our minimum probability test (
                # thus helping filter out weak detections)
                if confidence > 0.5:
                    # compute the (x, y)-coordinates of the bounding box for the face
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # extract the face ROI and grab the ROI dimensions
                    face = image[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]

                    # ensure the face width and height are sufficiently large
                    if fW < 20 or fH < 20:
                        continue

                    # construct a blob for the face ROI, then pass the blob through our face embedding model to
                    # obtain the 128-d quantification of the face
                    faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                                     (96, 96), (0, 0, 0), swapRB=True, crop=False)
                    self.embedder.setInput(faceBlob)
                    vec = self.embedder.forward()

                    # add the name of the person + corresponding face embedding to their respective lists
                    knownNames.append(name)
                    knownEmbeddings.append(vec.flatten())
                    total += 1

        # dump the facial embeddings + names to disk
        print("[INFO] serializing {} encodings...".format(total))
        data = {"embeddings": knownEmbeddings, "names": knownNames}
        f = open("FaceRecognition/output/embeddings.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()

    @staticmethod
    def trainData():
        print("[INFO] loading face embeddings...")
        data = pickle.loads(open("FaceRecognition/output/embeddings.pickle", "rb").read())

        # encode the labels
        print("[INFO] encoding labels...")
        le = LabelEncoder()
        labels = le.fit_transform(data["names"])

        # train the model used to accept the 128-d embeddings of the face and
        # then produce the actual face recognition
        print("[INFO] training model...")
        recognizer = SVC(C=1.0, kernel="linear", probability=True)
        recognizer.fit(data["embeddings"], labels)

        # write the actual face recognition model to disk
        f = open("FaceRecognition/output/recognizer.pickle", "wb")
        f.write(pickle.dumps(recognizer))
        f.close()

        # write the label encoder to disk
        f = open("FaceRecognition/output/le.pickle", "wb")
        f.write(pickle.dumps(le))
        f.close()
        print("[INFO] Training done!")

    def run(self) -> None:
        self.extractEmbedding()
        self.trainData()
