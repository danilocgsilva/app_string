import argparse
import os
from app_string.fn import getAppPath, getFileList, printPathAndContent
from app_string.NotValidPathException import NotValidPathException
from app_string.FileListConfig import FileListConfig

def generate(file_list_config: FileListConfig):
    try:
        appPath = getAppPath()
    except NotValidPathException as e:
        print(e)
        exit()

    fileList = getFileList(appPath, file_list_config)

    errorBag = []
    for fileEntry in fileList:
        printPathAndContent(fileEntry, errorBag, file_list_config, True)

    if errorBag:
        print("\nErrors encountered during file processing:")
        for error in errorBag:
            print(error)

