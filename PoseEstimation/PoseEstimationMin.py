import cv2 
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpPose=mp.solutions.pose
pose=mpPose.Pose()  

while True:
    sucess,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    print(results)
    if results
    cv2.imshow("Image",img)

    cv2.waitKey(1)
    
