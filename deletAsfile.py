
import imp
import shutil

import cv2
from colorama import Back ,Fore,Style
import pyttsx3
import cv2
engine = pyttsx3.init()
engine.setProperty('rate',130)

'''
def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect

        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        print(barcode_info)
        with open('C:\\Users\\admin\\Desktop\\main.py\\'+barcode_info+'\\'+'Qr'+barcode_info+'.txt', mode='w') as file:
            file.write( barcode_info)  
            
    return frame

def DeletFile():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()


def DElQR():
    file=open('C:\\Users\\admin\\Desktop\\main.py\\'+barcode_info+'\\'+'Qr'+barcode_info+'.txt', mode='r')    
    r=file.readline()
    
    return 0
    
'''
def seYou():
    cap=cv2.VideoCapture(0)
    detector=cv2.QRCodeDetector()
    while True:
        _,img=cap.read()
        data,one, _=detector.detectAndDecode(img)
        if data:
            a=data
            print(data)
            break
        cv2.imshow('ftv',img)
        if cv2.waitKey(1)==ord('q'):
            break
    try:
        shutil.rmtree(data)
        print(Fore.GREEN+' palak file is del ok .')
        engine.say(' palak file is dal ok .')
        engine.runAndWait()
    except IOError as e:
        print(Fore.RED+' im not find ........')
        engine.say('this name not have plak')
        engine.runAndWait()
        print(Fore.RED+e)    
     #  history   
    cv2.destroyAllWindows()
    import datetime
    now = datetime.datetime.now() 
    fo=open('histore.txt','a')
    sum='\n'+'plak name :'+str (data)+'|| time : '+now.strftime("%Y-%m-%d %H:%M:%S")
    fo.write(sum)
    fo.close()
    
    
    
    
          