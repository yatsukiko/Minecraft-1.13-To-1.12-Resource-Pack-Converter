import os
from dicto import blockDict, itemDict

def genPath(sub, item):
    return "assets/minecraft/models/{}/{}.json".format(sub, item)
    
for key, value in blockDict.items():
    try:
        os.rename(genPath("block", value), genPath("block", key))
        print("Successfully converted " + str(value) + ".json to " + str(key) + ".json")
    except:
        print("An error occured converting " + str(value) + ".json " + str(key) + ".json")

for key, value in itemDict.items():
    try:
        os.rename(genPath("item", value), genPath("item", key))
        print("Successfully converted " + str(value) + ".json to " + str(key) + ".json")
    except:
        print("An error occured converting " + str(value) + ".json to " + str(key) + ".json")
