from Lib import gui 
from Lib import sign
from Lib import speech
import PySimpleGUI as sg
a=0

  
password=sg.popup_get_text('Type your password to login',title="Sign language", password_char='*',size=(50, 2),  font='Arial')
if password == '58':
     while a!=3 :
        a=gui.gui()
        if a==1:
           sign.sign()
        if a==2:
           speech.speech()