
from pyFig import col
from plak import plak1 
from readDataAsfile import ReadDataAsFile
from deletAsfile import seYou
from oos import LoagindAnimatin
from colorama import Back ,Fore,Style
from countFol import hesab
import os
from fileTime import Ftime
import sys
from Komak import helpS

   
def Run1():
    

    LoagindAnimatin()
    os.system('cls')
    # vugar
    col()
    client=input(Fore.GREEN+' run pro[run] '+'\n'+ '\n'+Fore.BLUE+ ' help   [help] ' +'\n'+ '\n'+Fore.MAGENTA+' find  car [-f]  '+'\n'+ '\n'+Fore.YELLOW+' delet pro [ -r ] '+'\n'+'\n'+ Fore.WHITE+' have many save [-c ] '+'\n'+'\n'+Fore.RED+' time of save file  [-s]'+'\n'+'\n'+Fore.WHITE+' ----'+Fore.BLUE+'----'+Fore.CYAN+'----'+Fore.GREEN+'----'+Fore.MAGENTA+'----'+Fore.WHITE+'--->: ')
    if client == 'help':
        helpS()
        client9=input(Fore.GREEN+' for back -n '+'|'+Fore.RED+' for exit -x  : ') 
        if client9 == '-x':
            sys.exit()
            
        if client9 == '-n':
            Run1()
     
    if client == '-c':
        hesab()
        Run1()
        
    if client == '-f':
        ReadDataAsFile()
        client6=input(Fore.GREEN+' for back -n '+'|'+Fore.RED+' for exit -x  : ') 
        if client6 == '-x':
            sys.exit()
            
        if client6 == '-n':
            Run1()
     
    if client == '-s':
       
        Ftime()
        client5=input(Fore.GREEN+' for back -n '+'|'+Fore.RED+' for exit -x  : ') 
        if client5 == '-x':
            sys.exit()
            
        if client5 == '-n':
            Run1()
                
        
    if client == '-r':
        
        seYou()
        client4=input(Fore.GREEN+' for back -n '+'|'+Fore.RED+' for exit -x  : ') 
        if client4 == '-x':
            sys.exit()
            
        if client4 == '-n':
            Run1()
        
        
    if client == 'run':
        
        #pl=image.name
        #createFolder(image.name)
        plak1()
        
        client1=input(Fore.GREEN+' for back -n '+'|'+Fore.RED+' for exit -x  : ') 
        if client1 == '-x':
            sys.exit()
            
        if client1 == '-n':
            Run1()
        
    else :
        Run1()    

                      
Run1() 

       
