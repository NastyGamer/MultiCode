from Util import readInfo

def listInstances():
    for entry in readInfo()["instances"]:
        print("Name       → " + entry["name"])
        print("Created    → " + entry["creationDate"])
        print("Last Used  → " + entry["lastUsedDate"])
