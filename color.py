
import cv2
import numpy as np
from matplotlib import pyplot as plt
from regex import F, P
import image as m
import pyttsx3
from colorama import Back ,Fore,Style
engine = pyttsx3.init()
engine.setProperty('rate',130)

class color:
    def ColorCar(dim):
        im=m.name
        image = cv2.imread(im)
        image=cv2.resize(image,(300,300),cv2.INTER_AREA)
     # create NumPy arrays from the boundaries
        lower_red= np.array([17,15,100], dtype = "uint8")
        upper_red= np.array([33,33,255], dtype = "uint8")
 
        lower_blue= np.array([66,27,0], dtype = "uint8")
        upper_blue= np.array([255,243,69], dtype = "uint8")
 
        lower_green= np.array([12,38,0], dtype = "uint8")
        upper_green= np.array([84,255,190], dtype = "uint8")

        mask_red= cv2.inRange(image, lower_red, upper_red)
        output_red= cv2.bitwise_and(image, image, mask = mask_red)
 
        mask_blue= cv2.inRange(image, lower_blue, upper_blue)
        output_blue= cv2.bitwise_and(image, image, mask = mask_blue)
 
        mask_green= cv2.inRange(image, lower_green, upper_green)
        output_green= cv2.bitwise_and(image, image, mask = mask_green)

       
#lower_Black = np.array([0,0,0],dtype="uint8")
#upper_Black = np.array([50,50,100],dtype="uint8")
#mask_Black= cv2.inRange(image, lower_Black, upper_Black)
#output_Black= cv2.bitwise_and(image, image, mask = mask_Black)




    # show the images
        output1=np.hstack([image, output_red])
        output2=np.hstack([output_blue,output_green])
        output3=np.vstack([output1,output2])
        cv2.imshow("color",output3)
        print(Fore.GREEN+" The color of the car photo was recorded in its own folder")
        engine.say('The color of the car photo was recorded in its own folder')
        engine.runAndWait()
        addin='C:\\Users\\admin\\Desktop\\main.py\\'+dim+'\\'+'color '+dim+'.jpg'
        cv2.imwrite(addin,output3)
        cv2.waitKey(0) & 0xFF
        cv2.destroyAllWindows()
    