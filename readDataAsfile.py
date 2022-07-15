
from colorama import Back ,Fore,Style
from matplotlib import image
import time
import pyttsx3

import image
import cv2
engine = pyttsx3.init()
engine.setProperty('rate',130)

def ReadDataAsFile():
    
    cap=cv2.VideoCapture(0)
    detector=cv2.QRCodeDetector()
    while True:
        _,img=cap.read()
        data,one, _=detector.detectAndDecode(img)
        if data:
            a=data
            #print(data)
            break
        cv2.imshow('ftv',img)
        if cv2.waitKey(1)==ord('q'):
            break
    cv2.destroyAllWindows()
    a='C:\\Users\\admin\\Desktop\\main.py\\'+data+'\\'+data+'.txt'
    file = open( a, "r" )
    line=file.readlines()
    print(line)
    print()
    engine.say('done successfully')   
    engine.runAndWait()
    print( )
    file.close()
    time.sleep(5)
    
    
    
    


