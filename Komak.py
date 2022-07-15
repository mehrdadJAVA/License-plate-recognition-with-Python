import webbrowser
import pyttsx3

from colorama import Back ,Fore,Style
engine = pyttsx3.init()
engine.setProperty('rate',130)


    
    
def helpS():
    
    clx=input(Fore.MAGENTA+' Are you read = -r  &&  lisen = -i  && Open the sites of used libraries = -b : ')
    print()
    #read khode ensan
    if clx == '-r':
        print(Fore.WHITE+ ' This project has been done with some of the popular Python libraries. To run this program, you need to install the libraries. ')
        print(Fore.WHITE + ' It does not matter which version of the libraries you install, except , whose version must be 4.5.4.60. You run this.')
        
       
        
    #read robot
    if clx == '-i':
        engine.say(' It does not matter which version of the libraries you install, except [openCv], whose version must be 4.5.4.60. You run this.')
        engine.say(' This project has been done with some of the popular Python libraries. To run this program, you need to install the libraries')
        engine.runAndWait()
        
        
        
    #open broser
    if clx == '-b':
        webbrowser.open('https://opencv.org/')
        webbrowser.open('https://numpy.org/doc/stable/')
        webbrowser.open('https://imutils.readthedocs.io/en/latest/index.html')
        webbrowser.open('https://www.jaided.ai/easyocr/documentation/')
        

    
        