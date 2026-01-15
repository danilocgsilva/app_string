import argparse
import os
from fn import getAppPath, getFileList, printPathAndContent
from NotValidPathException import NotValidPathException

try:
    appPath = getAppPath()
except NotValidPathException as e:
    print(e)
    exit()

fileList = getFileList(appPath)

for fileEntry in fileList:
    printPathAndContent(fileEntry)
