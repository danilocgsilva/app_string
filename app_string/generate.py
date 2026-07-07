import argparse
import os
from app_string.fn import getAppPath, getFileList, printPathAndContent
from app_string.NotValidPathException import NotValidPathException
from app_string.FileListConfig import FileListConfig

def generate(file_list_config: FileListConfig, path=None):
    try:
        # Use provided path or prompt user
        if path:
            appPath = path
            if not os.path.exists(appPath):
                raise NotValidPathException(f"Invalid path: {appPath}")
        else:
            appPath = getAppPath()
    except NotValidPathException as e:
        print(e)
        exit()

    fileList = getFileList(appPath, file_list_config)

    errorBag = []
    for fileEntry in fileList:
        ignore_content = file_list_config.only_path
        printPathAndContent(fileEntry, errorBag, ignore_content, appPath)

    if errorBag:
        print("\nErrors encountered during file processing:")
        for error in errorBag:
            print(error)