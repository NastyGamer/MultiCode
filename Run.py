from Util import readInfo, writeInfo
from Create import parseInstanceNames
from colorama import Fore, Style
import subprocess

def runInstance():
    names = parseInstanceNames()
    name = ""
    while(True):
        name = input("Instance Name → ")
        if name in names:
            break
        else: print(Fore.RED + "No instance with that name exists" + Style.RESET_ALL)
    subprocess.call("instances/" + name + "/Code.exe")
    