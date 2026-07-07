import os
import re
from app_string.NotValidPathException import NotValidPathException
from typing import List, Iterator
from time import sleep
from app_string.FileListConfig import FileListConfig

def isValidPath(pathToValidate: str) -> bool:
    return os.path.exists(pathToValidate)

def getAppPath() -> str:
    pathToFetchContents = input("Type the file path to fetch all contents: ")
    
    if isValidPath(pathToFetchContents):
        return pathToFetchContents

    raise NotValidPathException(f"Invalid path: {pathToFetchContents}")

def getFileList(path: str, file_list_config: FileListConfig) -> Iterator[str]:
    """
    Yield all file paths under `path` recursively.
    Skips directories and follows symlinks if they point to files.
    """
    for root, dirs, files in os.walk(path):
        path_components = root.split("/")

        if file_list_config.ignore_git:
            if '.git' in path_components:
                continue

        if file_list_config.ignore_vendor:
            if 'vendor' in path_components:
                continue

        if file_list_config.ignore_var_cache:
            if 'var/cache' in root:
                continue

        for file_name in files:
            full_path = os.path.join(root, file_name)
            slice_index = len(path)
            relative_path = full_path[slice_index:]
            if file_list_config.regex_ignore:
                if re.compile(file_list_config.regex_ignore).search(relative_path):
                    continue

            if file_list_config.full_path:
                yield full_path
            else:
                slice_index = len(path)
                relative_path = full_path[slice_index:]
                yield relative_path

def printPathAndContent(
    fileEntry: str, 
    errorBag: List[str], 
    ignore_content: bool,
    path_to_append: str
) -> None:
    try:
        if not ignore_content:
            fileString = ""
            fileString += f"## {fileEntry}\n"
            fileString += "<start_of_content>\n"

            # full_path = f"{path_to_append}{fileEntry}"
            myFile = open(fileEntry, 'r', encoding='utf-8', errors='ignore')
            fileString += myFile.read()
            myFile.close()

            print(fileString)

            print(f"<end_of_content:{fileEntry}>")
        else:
            print(fileEntry)
    except Exception as e:
        errorString = f"Error reading file {fileEntry}: {e}"
        errorBag.append(errorString)