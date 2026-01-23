import argparse
import os
from app_string.fn import getAppPath, getFileList, printPathAndContent
from app_string.NotValidPathException import NotValidPathException

def generate():
    try:
        appPath = getAppPath()
    except NotValidPathException as e:
        print(e)
        exit()

    fileList = getFileList(appPath)

    errorBag = []
    for fileEntry in fileList:
        printPathAndContent(fileEntry, errorBag)

    if errorBag:
        print("\nErrors encountered during file processing:")
        for error in errorBag:
            print(error)

