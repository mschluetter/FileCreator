from fileinput import filename
import os
import json
from typing import List

class FileCreator:
    data: List

    def __init__(self, json_path:str=None, from_file:bool=True, data:List=None) -> None:
        if from_file:
            with open(json_path, "r", encoding="utf-8") as f:
                jdata = json.load(f)
            self.data = jdata["files"]
        else:
            self.data = data

    def run(self):
        for file in self.data:
            path = os.path.join(*file["path"])
            if not os.path.exists(path):
                os.makedirs(path)
            path = os.path.join(path, file["filename"])
            with open(path, "w", encoding="utf-8") as f:
                f.write(file["default"])

def main() -> None:
    creator = FileCreator("files.json")
    creator.run()


if __name__ == "__main__":
    main()