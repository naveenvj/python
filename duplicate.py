import os
import hashlib
import pprint

scanDir = '/home/hackme/Desktop/works/duplicate/conf'

hashDict = {}

def  addHash(fileName):
    hashObj = hashlib.new('md5')
    hashObj.update(open(fileName,'rb').read())
    hashValue = hashObj.hexdigest()
    if hashValue not in hashDict:
        hashDict[hashValue] = []
        hashDict[hashValue].append(fileName)
    else:
        hashDict[hashValue].append(fileName)


for  fileName in os.listdir(scanDir):
    abs_path = os.path.join(scanDir,fileName)    
    if os.path.isfile(abs_path):
        addHash(abs_path)

#pprint.pprint(hashDict)


for  fileList in hashDict.values():
    if len(fileList) > 1:
        print(fileList,len(fileList))






