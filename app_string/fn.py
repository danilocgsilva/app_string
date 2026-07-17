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

def read_ignore_files(base_path: str) -> List[re.Pattern]:
    ignore_patterns = []

    try:
        for filename in os.listdir(base_path):
            if filename.startswith('.app-string-ignore') and not filename.endswith('--deactivated'):
                file_path = os.path.join(base_path, filename)
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                    ignore_patterns.extend([re.compile(pattern) for pattern in patterns])
    except Exception as e:
        print(f"Warning: Could not read ignore files in {base_path}: {e}")

    return ignore_patterns

def getFileList(path: str, file_list_config: FileListConfig) -> Iterator[str]:
    """
    Yield all file paths under `path` recursively.
    Skips directories and follows symlinks if they point to files.
    """
    # Get ignore patterns from both CLI and file
    ignore_patterns = []

    # Add patterns from .app-string-ignore* files (excluding --deactivated ones)
    if file_list_config.ignore_file:
        ignore_patterns.extend(read_ignore_files(path))

    # Add patterns from command line regex
    if file_list_config.regex_ignore:
        try:
            ignore_patterns.append(re.compile(file_list_config.regex_ignore))
        except re.error as e:
            print(f"Warning: Invalid regex pattern '{file_list_config.regex_ignore}': {e}")

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
            relative_path = full_path[len(path):]

            # Check if file matches any ignore pattern
            should_ignore = False
            for pattern in ignore_patterns:
                if pattern.search(relative_path):
                    should_ignore = True
                    break

            if should_ignore:
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
