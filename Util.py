import json, platform

def getPlatform():
    return platform.system()

def readInfo():
    with open("info.json", "r") as f:
        return json.load(f)

def writeInfo(data):
    with open('info.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)