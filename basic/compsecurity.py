from os import access, name
import cv2
#import dropbox
import time 
import random

start_time = time.time()

def take_snap():
    number = random.randint(0,100)
    video_capture_obj = cv2.VideoCapture(0)
    result = True 
    
    while(result):
        ret,frame = video_capture_obj.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name , frame)
        start_time = time.time
        result = False
        
        return img_name
    print("snapshot taken")
    video_capture_obj.release()
    cv2.destroyAllWindows()
    
def upload_file(img_name) :
    #accesstoken = "sl.A9VH8oDNto0OmCdyunyhayJref7Aw2qmGZx0xl8UhmKlFFKpbE7jo6qIATLDLsy9jXWKq6HvMnzab7GjutI0c_fUvgPGP9CQRp6kBmB_zRc8QOGuFfoG9E6koZqE-yh4vZgXkeA"
    file = img_name
    filefrom = file
    #fileto = "/newfolder1/" + (img_name)
    #dbx = dropbox.Dropbox(accesstoken)
    
    #with open (filefrom , 'rb') as f : 
     #   dbx.files_upload(f.read(), fileto , mode = dropbox.files.WriteMode.overwrite)
        
      #  print("file uploaded")
        
def main():
   while (True):
    if ((time.time()-start_time)>=1):
        name = take_snap()
        upload_file(name)
            
main()