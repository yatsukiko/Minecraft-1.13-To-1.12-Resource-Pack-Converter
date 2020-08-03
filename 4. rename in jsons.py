import fileinput
from pathlib import Path
from dicto import blockDict
import glob


print("Batch block names in jsons file started")
fJsons = list(Path("assets/minecraft/models/block/.").rglob("*.[jJ][sS][oO][nN]"))
for key, value in blockDict.items():
    try:
        with fileinput.FileInput(fJsons, inplace=True) as file:
            for line in file:
                print(line.replace(value + '"', key + '"'), end='')
        print("Trying to write to " + str(value) + ".json")
    except:
        print("An error occured renaming in " + str(value) + ".json")