from Util import readInfo, writeInfo
from Create import parseInstanceNames
from colorama import Fore, Style

def deleteInstance():
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
             info["instances"].pop(i)
             break
    writeInfo(info)

