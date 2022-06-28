import cv2
import dropbox
import time
import random
start_time=time.time()
# defining a function take_snapshot()
def take_snapshot():
    number=random.randint(1,100)
    # initializing the cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame = videoCaptureObject.read()
        ing_name="ing_"+str(number)+".png"
        cv2.imwrite(ing_name,frame)
        start_time=time.time
        result=False
    return ing_name
def upload_file(ing_name):
    access_token="sl.BJiUs2bFRKFwZ-6tRSp2H70NbhMOQJ46O-loApVjnzHlDbLPpWnis24JzYxFeHZ9tgklY8TqLmamlkjsR0-9NcuyTUoPiIwOqY4S8MgOIa9spV6SE_q_2rah8f4aeshd3qw_RkSM2K65"
    file=ing_name
    file_from=file
    file_to="/test"+file
    dbx = dropbox.Dropbox(access_token)
    # open the file and upload it
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED :)")
def main():
    while(True):
        if(time.time()-start_time>=5):
            name=take_snapshot()
            upload_file(name)
main()