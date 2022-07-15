import os
from colorama import Back ,Fore,Style
import time


def LoagindAnimatin():
    for i in range(4):
        os.system('cls')
        print(Fore.GREEN+' loading .')
        time.sleep(0.5)
        os.system('cls')
        print(Fore.WHITE+' loading . .')
        time.sleep(0.5)
        os.system('cls')
        print(Fore.GREEN+' loading . . .')
        time.sleep(0.5)
        
