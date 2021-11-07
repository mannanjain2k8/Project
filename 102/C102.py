import cv2
import dropbox
import random
import time

start_time = time.time()

def takesnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False
    return img_name
    print("Snapshot Taken")
    


    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    accessToken = "kM_cQWOzpkYAAAAAAAAAAf8IoO1XdJw-6jSNOFUmcXaCgBFxkY3U1MJG6IoHr5QG"
    file = img_name
    file_from = file
    file_to = "/testFolder/" + (img_name)
    dbx = dropbox.Dropbox(accessToken)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overWrite)
        print("file_uploaded")

def main():
    while(True):
        if((time.time() - start_time)>= 1):
            name = takesnapshot()
            uploadFile(name)  


main()