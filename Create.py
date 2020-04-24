from Util import readInfo, getPlatform, writeInfo
from datetime import date
import requests, shutil, os
from colorama import Fore, Style

def createInstance():
    names = parseInstanceNames()
    name = ""
    while(True):
        name = input("Instance Name → ")
        if not name in names:
            break
        else: print(Fore.RED + "An instance with that name already exists" + Style.RESET_ALL)
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
        print(Fore.CYAN + "Detected OS: " + plat + Style.RESET_ALL)
        print(Fore.YELLOW + "Fetching VSCode..." + Style.RESET_ALL)
        url = "https://go.microsoft.com/fwlink/?Linkid=850641"
        open("tmp.zip", "wb").write(requests.get(url).content)
    elif(plat == "Linux"):
        print(Fore.YELLOW + "Fetching VSCode..." + Style.RESET_ALL)
        url = "https://go.microsoft.com/fwlink/?LinkID=620884"
        open("tmp.tar.gz", "wb").write(requests.get(url).content)
    elif(plat == "Darwin"):
        print(Fore.RED + "MacOS is not yet implemented" + Style.RESET_ALL)
        exit(0)
    else:
        downloadFile(input(Fore.RED + "Could not determin the OS. Please input the OS manually (Windows, Linux, Darwin" + Style.RESET_ALL))
    print(Fore.GREEN + "Done Fetching VSCode..." + Style.RESET_ALL)

def extractFile(name):
    if(not os.path.exists("instances/")):
        print(Fore.YELLOW + "Creating instances folder..." + Style.RESET_ALL)
        os.mkdir("instances")
        print(Fore.GREEN + "Done creating instances folder..." + Style.RESET_ALL)
    print(Fore.YELLOW + "Extracting VSCode..." + Style.RESET_ALL)
    plat = getPlatform()
    if(plat == "Windows"):
         shutil.unpack_archive("tmp.zip", "instances/" + name)
    elif(plat == "Linux"):
         shutil.unpack_archive("tmp.tar.gz", "instances/" + name)
    elif(plat == "Darwin"):
        print(Fore.RED + "MacOS is not yet implemented" + Style.RESET_ALL)
        exit(0)
    print(Fore.GREEN + "Done extracting VSCode..." + Style.RESET_ALL)

def createDataDir(name):
    print(Fore.YELLOW + "Creating data dir..." + Style.RESET_ALL)
    os.mkdir("instances/" + name + "/data")
    print(Fore.GREEN + "Done creating data dir..." + Style.RESET_ALL)

def deleteTmp():
    print(Fore.YELLOW + "Cleaning up..." + Style.RESET_ALL)
    plat = getPlatform()
    if(plat == "Windows"):
        os.remove("tmp.zip")
    elif(plat == "Linux"):
        os.remove("tmp.tar.gz")
    elif(plat == "Darwin"):
        print(Fore.RED + "MacOS is not yet implemented" + Style.RESET_ALL)
        exit(0)
    print(Fore.GREEN + "Done cleaning up" + Style.RESET_ALL)

def registerInJson(name):
    print(Fore.YELLOW + "Registering instance..." + Style.RESET_ALL)
    info = readInfo()
    info["instances"].append({
        "name" : name, 
        "creationDate" : date.today().strftime("%d.%m.%Y"), 
        "lastUsedDate":"1.1.2000"
        })
    writeInfo(info)
    print(Fore.GREEN + "Done registering instance..." + Style.RESET_ALL)
