import os
import datetime
import cv2
def Ftime():
        
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
    path = r"C:\\Users\\admin\\Desktop\\main.py\\"+data+"\\"+data+".txt"
    c_time = os.path.getctime(path)
    dt_c = datetime.datetime.fromtimestamp(c_time)
    print(' Created on :', dt_c,'\n')
