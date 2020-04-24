from Util import readInfo, writeInfo
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
    subprocess.call("instances/" + name + "/Code.exe")
    