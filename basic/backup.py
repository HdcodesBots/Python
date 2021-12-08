import os
import shutil 

source = input("source folder name : ")
destination = input (" back up directory : ")

source = source + "/"
destination = destination + "/"

list_of_files = os.listdir(source)

for file in list_of_files : 
    shutil.copy((source + file) , destination)