import PySimpleGUI as sg

import cv2

import numpy as np

import time

import os

import speech_recognition as sr

from gtts import gTTS

from playsound import playsound

from Lib import HandTrackingModule as htm
def sign():
  layout = [

        [sg.Text("Sign To Speech",size=(30, 1), justification='center', font='Helvetica 20')],
        [sg.Image(filename="", key="-IMAGE-")],
        #[sg.Text(("Press Record To Start..."),size=(20, 1),font='Arial', key="word", justification="left")],
        [sg.Text(size=(20, 1),font='Arial', key="word"),],[sg.Button("Exit", size=(10, 1),)]]
  window = sg.Window("Sign To Speech",layout, location=(350, 100),element_justification='center')

  wCam, hCam = 640, 480

 

  cap = cv2.VideoCapture(0)

  cap.set(3, wCam)

  cap.set(4, hCam)
  folderPath = "FingerImages"
  folderPath2 = "sound"
  myLists = os.listdir(folderPath)
  myList=sorted(myLists) 
  with open('word.txt') as f:
      myListword=f.read().splitlines() 
  myListsounds = os.listdir(folderPath2)
  myListsound=sorted(myListsounds)
  

  overlayList = []




  for imPath in myList:

      image = cv2.imread(f'{folderPath}/{imPath}')


      overlayList.append(image)


  pTime = 0
  a=0
  v=""
  index=0
  oldindex=0


  detector = htm.handDetector(detectionCon=1)

 

  tipIds = [4, 8, 12, 16, 20]

 

  while True:
      
      event, values = window.read(timeout=20)
      if event == "Exit" or event == sg.WIN_CLOSED:
            window.close()
            break

      success, img = cap.read()

 

      img = detector.findHands(img)

      lmList = detector.findPosition(img, draw=False)

      #print(lmList)
      fingers=[]
      

      if len(lmList) != 0:
        if lmList[4][1] > lmList[3 ][1]:
           a=3
         

        else:
           a=1
        fingers.append(a)
      


         

        for id in range(1, 5):
      
        
          if lmList[tipIds[id]][2] < lmList[tipIds[id] - 1][2]:
                 a=3
          else:
               if lmList[tipIds[id] - 1][2] < lmList[tipIds[id] - 2][2]:
                 a=2
               else:
                 a=1
          fingers.append(a)
          
        z=[str(y)for y in fingers]
        az="".join(z)
        finger=str(az)
        v=finger+".jpg" 
        for i in range(0,len(myList)): 
           if v==myList[i]:
              index=i

        h, w, c = overlayList[index].shape

        img[0:h, 0:w] = overlayList[index]

 

        #cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 224), cv2.FILLED)

     

 

      cTime = time.time()

      fps = 1 / (cTime - pTime)

      pTime = cTime

 

      cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,

                  3, (191 ,239 ,255), 3)

 

      imgbytes = cv2.imencode(".png",img)[1].tobytes()

      window["-IMAGE-"].update(data=imgbytes)
      window.refresh() 
      #cv2.imshow("Image", img)
      if index!=oldindex :
  
         window["word"].update(myListword[index])
         window.refresh()
         k="sound/"+myListsound[index]
         playsound(k,False)
         oldindex=index
         
      
      #closed = cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1
      # if user closed window or if some key pressed
      # if closed:
      #         break
  cap.release()
  