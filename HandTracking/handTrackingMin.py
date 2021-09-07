
'''
This is basic code that enable you to read hands and detect evrey point in the hand
so you can do the applications that you want



'''
import cv2
import mediapipe as mp

import time
cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands = mpHands.Hands(max_num_hands=3)
mpDraw=mp.solutions.drawing_utils
pTime=0
while True :
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks: #if the there are some hand
        for hand in results.multi_hand_landmarks: #pass over every hand in the video
            for id,lm in enumerate(hand.landmark): #pass over every point in the hand
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h) #the x,y codenates of the hand
                cv2.putText(img,str(id),(int(cx),int(cy)),cv2.FONT_HERSHEY_PLAIN,3,(255,8,255),3) # write the cordenates in the picture
              
            mpDraw.draw_landmarks(img,hand,mpHands.HAND_CONNECTIONS)

    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,8,255),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
