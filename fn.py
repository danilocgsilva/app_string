import os
from NotValidPathException import NotValidPathException
from typing import List, Iterator

def isValidPath(pathToValidate: str) -> bool:
    return os.path.exists(pathToValidate)

def getAppPath() -> str:
    pathToFetchContents = input("Type the file path to fetch all contents: ")
    
    if isValidPath(pathToFetchContents):
        return pathToFetchContents

    raise NotValidPathException(f"Invalid path: {pathToFetchContents}")


def getFileList(path: str) -> Iterator[str]:
    """
    Yield all file paths under `path` recursively.
    Skips directories and follows symlinks if they point to files.
    """
    for root, dirs, files in os.walk(path):
        for name in files:
            yield os.path.join(root, name)

def printPathAndContent(fileEntry: str):
    print(f"## {fileEntry}")
    print("<start_of_content>")

    myFile = open(fileEntry)
    print(myFile.read())
    myFile.close()

    print("<end_of_content>")
