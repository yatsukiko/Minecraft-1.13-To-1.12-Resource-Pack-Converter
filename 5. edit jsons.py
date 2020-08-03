import fileinput
from pathlib import Path

fJsons = list(Path("assets/minecraft/models/block/.").rglob("*.[jJ][sS][oO][nN]"))

print("Batch block/blocks renaming in jsons files started.")
with fileinput.FileInput(fJsons, inplace=True) as file:
    for line in file:
        print(line.replace("block", "blocks"), end='')
with fileinput.FileInput(fJsons, inplace=True) as file:
    for line in file:
        print(line.replace("blockss", "blocks"), end='')
with fileinput.FileInput(fJsons, inplace=True) as file:
    for line in file:
        print(line.replace('"parent": "blocks/', '"parent": "block/'), end='')
with fileinput.FileInput(fJsons, inplace=True) as file:
    for line in file:
        print(line.replace('/blocks', '/block'), end='')