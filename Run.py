from Util import readInfo, writeInfo
from Create import parseInstanceNames
import subprocess

def runInstance():
    names = parseInstanceNames()
    name = ""
    while(True):
        name = input("Instance Name → ")
        if name in names:
            break
        else: print("No instance with that name exists")
    subprocess.call("instances/" + name + "/Code.exe")
    