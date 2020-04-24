from Util import readInfo, getPlatform, writeInfo
from datetime import date
import requests, shutil, os

def createInstance():
    names = parseInstanceNames()
    name = ""
    while(True):
        name = input("Instance Name → ")
        if not name in names:
            break
        else: print("An instance with that name already exists")
    downloadFile()
    extractFile(name)
    createDataDir(name)
    deleteTmp()
    registerInJson(name)

def parseInstanceNames():
    names = []
    for entry in readInfo()["instances"]:
        names.append(entry["name"])
    return names

def downloadFile():
    plat = getPlatform()
    if(plat == "Windows"):
        print("Detected OS: " + plat)
        print("Fetching VSCode...")
        url = "https://go.microsoft.com/fwlink/?Linkid=850641"
        open("tmp.zip", "wb").write(requests.get(url).content)
    elif(plat == "Linux"):
        print("Fetching VSCode...")
        url = "https://go.microsoft.com/fwlink/?LinkID=620884"
        open("tmp.tar.gz", "wb").write(requests.get(url).content)
    elif(plat == "Darwin"):
        print("MacOS is not yet implemented")
        exit(0)
    else:
        downloadFile(input("Could not determin the OS. Please input the OS manually (Windows, Linux, Darwin"))
    print("Done Fetching VSCode...")

def extractFile(name):
    print("Extracting VSCode...")
    plat = getPlatform()
    if(plat == "Windows"):
         shutil.unpack_archive("tmp.zip", "instances/" + name)
    elif(plat == "Linux"):
         shutil.unpack_archive("tmp.tar.gz", "instances/" + name)
    elif(plat == "Darwin"):
        print("MacOS is not yet implemented")
        exit(0)
    print("Done extracting VSCode...")

def createDataDir(name):
    print("Creating data dir...")
    os.mkdir("instances/" + name + "/data")
    print("Done creating data dir...")

def deleteTmp():
    print("Cleaning up...")
    plat = getPlatform()
    if(plat == "Windows"):
        os.remove("tmp.zip")
    elif(plat == "Linux"):
                os.remove("tmp.tar.gz")
    elif(plat == "Darwin"):
        print("MacOS is not yet implemented")
        exit(0)
    print("Done cleaning up")

def registerInJson(name):
    print("Registering instance...")
    info = readInfo()
    info["instances"].append({
        "name" : name, 
        "creationDate" : date.today().strftime("%d.%m.%Y"), 
        "lastUsedDate":"1.1.2000"
        })
    writeInfo(info)
    print("Done registering instance...")
