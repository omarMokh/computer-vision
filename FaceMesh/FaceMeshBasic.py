import cv2 
import mediapipe as mp
import time
from mediapipe.python.solutions import face_detection

from mediapipe.python.solutions.face_mesh import FaceMesh

cap=cv2.VideoCapture(0)

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
FaceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)

while True:
    scuess, img=cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=FaceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, face,mpFaceMesh.FACEMESH_CONTOURS) #we can try also face connections


    cv2.imshow("Image",img)
    cv2.waitKey(1)