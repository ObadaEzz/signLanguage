import PySimpleGUI as sg

def gui():
   file_list_column = [
           [sg.Text(text = "Sign language", size=(30, 1), justification='center', font='Helvetica 20')],

           [sg.Button('Sign To Speech',key='sign',size=(50, 3),  font='Arial')],
           [sg.Button('Speech To sign',key='speech',size=(50, 3),  font='Arial')]]





   layout = [[   sg.Column(file_list_column),]]

   window = sg.Window("Sign language", layout, element_justification='center')



   while True:

       event, values = window.read()
   

       if event == "Exit" or event == sg.WIN_CLOSED:

           window.close()
           return(3)

       if event=='sign':
           window.close()         
           return(1)
       if event=='speech':
           window.close()
           return(2)
           
    


   