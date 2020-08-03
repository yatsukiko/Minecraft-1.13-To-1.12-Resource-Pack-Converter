import os
from dicto import blockDict, itemDict

def genPath(sub, item):
    return "assets/minecraft/textures/{}/{}.png.mcmeta".format(sub, item)

for key, value in blockDict.items():
    try:
        os.rename(genPath("block", value), genPath("block", key))
        print("Successfully converted " + str(value) + ".png.mcmeta to " + str(key) + ".png.mcmeta")
    except:
        print("An error occured converting " + str(value) + ".png.mcmeta to " + str(key) + ".png.mcmeta")

for key, value in itemDict.items():
    try:
        os.rename(genPath("item", value), genPath("item", key))
        print("Successfully converted " + str(value) + ".png.mcmeta to " + str(key) + ".png.mcmeta")
    except:
        print("An error occured converting " + str(value) + ".png.mcmeta to " + str(key) + ".png.mcmeta")