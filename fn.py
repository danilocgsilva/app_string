import os
from NotValidPathException import NotValidPathException

def isValidPath(pathToValidate: str) -> bool:
    return os.path.exists(pathToValidate)

def getAppPath() -> str:
    pathToFetchContents = input("Type the file path to fetch all contents: ")
    
    if isValidPath(pathToFetchContents):
        return pathToFetchContents

    raise NotValidPathException(f"Invalid path: {pathToFetchContents}")
