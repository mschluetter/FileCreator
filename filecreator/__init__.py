import os
import json
from typing import List

class FileCreator:
    data: List = None # List of Dicts to create the Files

    def __init__(self, json_path:str=None, data:List=None, 
            json_key:str=None, json_position:int=0) -> None:
        """ Provide json path here. If you have the data,
        set from_file=False, and attach data."""

        if json_path:
            with open(json_path, "r", encoding="utf-8") as f:
                jdata = json.load(f)

            key = json_key if json_key else list(jdata.keys())[json_position]
            self.data = jdata[key]

        if data:
            if self.data:
                for entry in data:
                    self.data.append(entry)
            else:
                self.data = data
            
    def run(self) -> None:
        """ run this method to execute """
        for file in self.data:
            if len(file["path"]) == 0:
                path = ""
            else:
                path = os.path.join(*file["path"])
                if not os.path.exists(path):
                    os.makedirs(path)
            path = os.path.join(path, file["filename"])
            with open(path, "w", encoding="utf-8") as f:
                f.write(file["default"])

if __name__ == "__main__":
    print("Welcome to file creator. Please import the FileCreator class.")