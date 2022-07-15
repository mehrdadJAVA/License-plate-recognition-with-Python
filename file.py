import os
from colorama import Back ,Fore,Style
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',130)


    

def createFolder(directory):
    try:
        
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(Fore.GREEN+'cerat sucsufully')
            engine.say('file creat to this folder ')
            engine.runAndWait()
    except OSError:
        print (Fore.RED+'Error: Creating directory. ' +  directory)
        engine.say('folder not cerated but folder is exsist')
        engine.runAndWait()
        


