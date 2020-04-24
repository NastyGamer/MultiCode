from Util import readInfo
from colorama import Fore, Style

def listInstances():
    for entry in readInfo()["instances"]:
        print(Fore.CYAN + "Name       → " + entry["name"] + Style.RESET_ALL)
        print(Fore.CYAN + "Created    → " + entry["creationDate"] + Style.RESET_ALL)
        print(Fore.CYAN + "Last Used  → " + entry["lastUsedDate"] + Style.RESET_ALL + "\n")