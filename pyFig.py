
import pyfiglet
from termcolor import colored
def col():
    color='red'  
    result = pyfiglet.figlet_format("VUGAR")
    result=colored(result,color=color)
    print(result)