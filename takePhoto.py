import cv2 



def photo(nme):
    cam = cv2.VideoCapture(0)

    count = 0

    while True:
        ret, img = cam.read()

        cv2.imshow("take your photo else not countinie app", img)

        if not ret:
           break
 
        k=cv2.waitKey(1)

        if k%256==27:
        #For Esc key
            print(" Close")
            break
        elif k%256==32:
        #For Space key

            print(" save ok " +str(count)+ " saved")
            file='C:\\Users\\admin\\Desktop\\main.py\\'+nme+'\\'+'human '+nme+'.jpg'
            cv2.imwrite(file, img)
            count +=1