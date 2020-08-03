import fileinput
from pathlib import Path

print("Changing pack.mcmeta version.")

with fileinput.FileInput("pack.mcmeta", inplace=True) as file:
    for line in file:
        print(line.replace('"pack_format": 4,', '"pack_format": 3,'), end='')