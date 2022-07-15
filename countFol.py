
import os
import time
from colorama import Back ,Fore,Style

def hesab():
    files = folders = 0

    for _, dirnames, filenames in os.walk('C:\\Users\\admin\\Desktop\\main.py'):
  # ^ this idiom means "we won't be using this value"
        files += len(filenames)
        folders += len(dirnames)
    folders-=10  
    if folders <1:
        print(Fore.RED+" dont have plak  :|")
    if folders >= 1 :     
        for i in range(4):
            os.system('cls')
            print(folders)
            time.sleep(0.5)
            os.system('cls')
            print(folders)
            time.sleep(0.5)
            os.system('cls')
            print(folders)
            time.sleep(0.5)
            
        