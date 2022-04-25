#!/usr/bin/env python
# coding: utf-8
# # Managing Google Drive using Python
#Import modules
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
# Rename the downloaded JSON file to client_secrets.json which downloaded from the googleapi
# The client_secrets.json file needs to be in the same directory as the script.
gauth = GoogleAuth()
drive = GoogleDrive(gauth)
# # Upload files to your Google Drive
upload_file_list = ['Receipt2.HEIC']
for upload_file in upload_file_list:
    gfile = drive.CreateFile({'parents': [{'id': '1Tp083pQkYcEsekoGrEw3ComylNvcrWsQ'}]})
# Read file and set it as a content of this instance.
    gfile.SetContentFile(upload_file)
    gfile.Upload() # Upload the file.
# # List all files from the specific folder 
file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1Tp083pQkYcEsekoGrEw3ComylNvcrWsQ')}).GetList()
for file in file_list:
    print('title: %s, id: %s' % (file['title'], file['id']))
# # Download every file in folder
for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
    print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
file.GetContentFile(file['title'])
# ## Create text file in drive
file1 = drive.CreateFile({
    'parents': [{'id': '1Tp083pQkYcEsekoGrEw3ComylNvcrWsQ'}],
    'title': 'SWDVPhotos.txt'})  # Create a GoogleDriveFile instance with title 'test.txt'.
file1.SetContentString('Hello World!') # Set content of the file from the given string.
file1.Upload()
# ## read the file directly from Google Drive
##file2 = drive.CreateFile({'id': file1['id']})
##file2.GetContentString('SWDVPhotos.txt')