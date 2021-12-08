import pyfiglet
import os
import random

os.system('cls')

default = input("Enter anything that you want to convert to ascii art :")
text = pyfiglet.figlet_format(default , )
print(text)