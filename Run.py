from Util import readInfo, writeInfo, getPlatform
from Create import parseInstanceNames
from colorama import Fore, Style
from datetime import date
import subprocess

def runInstance():
    names = parseInstanceNames()
    name = ""
    while(True):
        name = input("Instance Name → ")
        if name in names:
            break
        else: print(Fore.RED + "No instance with that name exists" + Style.RESET_ALL)
    info = readInfo()
    for i in range(len(info["instances"])):
        if(info["instances"][i]["name"] == name):
             info["instances"][i]["lastUsedDate"] = date.today().strftime("%d.%m.%Y")
             break
    writeInfo(info)
    plat = getPlatform()
    if(plat == "Windows"):
            subprocess.call("instances/" + name + "/Code.exe")
    elif(plat == "Linux"):
           subprocess.call("instances/" + name + "/VSCode-linux-x64/Code.exe")
    elif(plat == "Darwin"):
        print(Fore.RED + "MacOS is not yet implemented" + Style.RESET_ALL)
        exit(0)
    