import os

import speech_recognition as sr

from gtts import gTTS

from playsound import playsound

from PIL import Image, ImageTk

import PySimpleGUI as sg

def speech():
   currentfolder=os.getcwd()
   folderPath = currentfolder+"/FingerImages"
   myLists = os.listdir(folderPath)
   myList=sorted(myLists) 
   with open('word.txt') as f:
      myListsound=f.read().splitlines() 
   nospeech=1
   photoindex=1000

   file_list_column = [
   
           [sg.Text(text = "Speech To Sign",size=(20, 1), justification='center', font='Helvetica 20')],

           [sg.Button('Record',key='record',size=(40, 2),font='Arial',focus=True)],
           [sg.Button('Back',key='back',size=(40, 2),font='Arial',focus=True)],]
   image_viewer_column = [
               [sg.Text(("Press Record To Start..."),size=(20, 1),font='Arial', key="-TOUT-", justification="left")],
               [sg.Image(size=(250, 250),key="image")], ]
   layout = [[

        sg.Column(file_list_column),

        sg.VSeperator(),

        sg.Column(image_viewer_column),

         ]]

   window = sg.Window("Sign language", layout,element_justification='center',margins=(0, 0), finalize=True,location=(400, 200))
   image = Image.open(currentfolder+'/Lib/w.jpg')
   new_image = image.resize((250, 250))
                         
                         
   photo_img = ImageTk.PhotoImage(new_image)
   window["image"].update(data=photo_img)
   window["-TOUT-"].update("Press Record to start")   
   
   while True:
       event, values = window.read()
       if event == "Exit" or event == sg.WIN_CLOSED or event=='back':

           break
           

       if event=='record':
           image = Image.open(currentfolder+'/Lib/w.jpg')
           new_image = image.resize((250, 250))              
           photo_img = ImageTk.PhotoImage(new_image)
           window["image"].update(data=photo_img)  
           window.refresh() 
           r = sr.Recognizer()
 
           with sr.Microphone() as source:
               r.adjust_for_ambient_noise(source)
               window["-TOUT-"].update("Please say something...")
               window.refresh() 

               
               audio = r.listen(source)
                  
 
                  
 
               try:
                  window["-TOUT-"].update("recognize,Please wait...")
                  window.refresh() 
               
                  rec=r.recognize_google(audio,language ="ar-AR")
                  
               except Exception as e:
                  window["-TOUT-"].update("Sorry,I didn't understand")
                  window.refresh() 
                  nospeech=0  
               if nospeech!=0:
                 for id in range(0,len(myListsound)): 
                    if rec==myListsound[id]:
                       photoindex=id
                       break
                    else:
                       photoindex=100
                 if photoindex==100:
                   window["-TOUT-"].update("What do you mean?!")
                   image = Image.open(currentfolder+'/Lib/ops.jpg')
                   new_image = image.resize((250, 250))              
                   photo_img = ImageTk.PhotoImage(new_image)
                   window["image"].update(data=photo_img)  
                   window.refresh()
                   window.refresh() 
                 else:
                   image = Image.open(folderPath+'/'+myList[photoindex])
                   new_image = image.resize((250, 250))  
                   photo_img = ImageTk.PhotoImage(new_image)
                   window["image"].update(data=photo_img)   
                   window["-TOUT-"].update("Done...")
                   window.refresh() 
           

   window.close()

           