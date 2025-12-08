import argparse
import os

def isValidPath(pathToValidate: str) -> bool:
    return os.path.exists(pathToValidate)

pathToFetchContents = input("Type the file path to fetch all contents: ")
if isValidPath(pathToFetchContents):
    print(f"The given path is {pathToFetchContents} and is valid.")
else:
    print(f"The given path is {pathToFetchContents} and is not valid.")


