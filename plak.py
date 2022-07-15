import imp
import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as plt
from colorama import Back ,Fore,Style
import datetime
import pyttsx3
import image
from takePhoto import photo
import os
from file import createFolder
from color import color
engine = pyttsx3.init()
import qrcode
engine.setProperty('rate',130)





def plak1():
    
    sum=image.name
    img = cv2.imread(sum)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(bfilter, 30, 200)


    keyPoint = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keyPoint)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
      # print(contours)

    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx

            break

    mask = np.zeros(gray.shape)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)


    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2+1, y1:y2+1]

    reader = easyocr.Reader(['id', 'en'])
    result = reader.readtext(cropped_image)
    
    # print(Fore.GREEN+' name of plak -->',result)

    m=result
    plate_text = m[0][-2]
    print(Fore.GREEN+'plak  :',plate_text)
    engine.say('plal is printed')
    engine.runAndWait()

        # برداشت پلاک از مانتریس 
    
    # list=[]
    # list.append(result)
    # mm=list[0]
    # strg = str(mm)
    # print('list =',list)
    # print('mm---->',strg)
    # print(type(strg))
    # revrsd = strg[::-1]
    # rs=revrsd[0:40]
    # se=rs[::-1]
    # print('rev ',se[0:36])
    # print(se[::-1])
    # print(se[:16])
    # de=se[:16]
    # de1=de[::-1]
    # print('=======',de1[:7])
    # de2=de1[:7]
    # print('make ;',de2[::-1])
    # de3=de2[::-1]
    # # os.system('cls')
    # print(de3)
    

    
    createFolder(plate_text)
    photo(plate_text)
    
    
    #save plak num to txt file in khode name
    def textAdd():
        i3=image.name
        now = datetime.datetime.now() 
        print ( ' '+now.strftime("%Y-%m-%d %H:%M:%S" ))
        a='C:\\Users\\admin\\Desktop\\main.py\\'+plate_text+'\\'+plate_text+'.txt'
        file = open( a, "w" )
        file.write('plak--=> '+plate_text+'\n'+'time --=> '+now.strftime("%Y-%m-%d %H:%M:%S" ))
        print(Fore.GREEN+' write ok to ---> ',a)
        print()
        engine.say('write plack to txt file ')
        engine.runAndWait()
        print( )
        
            # Q R code 

        nb=qrcode.make(plate_text)
        nb.save('C:\\Users\\admin\\Desktop\\main.py\\'+plate_text+'\\'+plate_text+'Q'+'.jpg')

        file.close()
         
   
    text = result[0][-2]
    font = cv2.FONT_HERSHEY_SIMPLEX
    res = cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1]+60),
    fontFace=font, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

    res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0, 255, 0), 3)
    cv2.imshow("Plate ", res)

        #plak galeeb
    textAdd()
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)
    plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
        # save picture to in picture name foldr
    po=image.name
    addin='C:\\Users\\admin\\Desktop\\main.py\\'+plate_text+'\\'+plate_text+'.jpg'
    status = cv2.imwrite(addin,new_image)
    print(Fore.GREEN+" Image written to file-system : ",status)
    color.ColorCar(plate_text)
    plt.show()
    cv2.waitKey(0)
     
    #  whatsapp
    '''
    def send():
        import pywhatkit
        import datetime
        ti= datetime.datetime.now()
        mi=ti.minute+2
        
        phone=input('enter your phone number ..')
        pywhatkit.sendwhatmsg("+98"+phone, "hellow this is your : "+de3, ti.hour,mi )

    send()
    '''
    

    
   
   
   

