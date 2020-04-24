from Create import parseInstanceNames
from Util import getPlatform, readInfo
from colorama import Fore, Style
import os

def showInfo():
    names = parseInstanceNames()
    name = ""
    while(True):
        name = input("Instance Name → ")
        if name in names:
            break
        else: print(Fore.RED + "No instance with that name exists" + Style.RESET_ALL)
    print(Fore.CYAN + "Name            → " + getName(name))
    print("Creation Date   → " + getCreationDate(name))
    print("Last Used Date  → " + getLastUsedDate(name))
    print("Extensions:")
    for e in getExtensions(name):
        print("                → " + e)
    print(Style.RESET_ALL)
    

def getExtensions(name):
    extensions = []
    path = ""
    plat = getPlatform()
    if(plat == "Windows"):
        path = "instances/" + name + "/data/extensions"
    elif(plat == "Linux"):
        path = "instances/" + name + "/VSCode-linux-x64/data/extensions"
    elif(plat == "Darwin"):
        print(Fore.RED + "MacOS is not yet implemented" + Style.RESET_ALL)
        exit(0)
    for file in os.listdir(path):
        extensions.append(file)
    return extensions

def getName(name):
    return name

def getCreationDate(name):
    info = readInfo()
    for i in range(len(info["instances"])):
        if(info["instances"][i]["name"] == name):
            return info["instances"][i]["creationDate"]

def getLastUsedDate(name):
    info = readInfo()
    for i in range(len(info["instances"])):
        if(info["instances"][i]["name"] == name):
            return info["instances"][i]["lastUsedDate"]

