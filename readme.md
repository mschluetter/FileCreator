# FileCreator
This file creator creates files based on the given parameters. You can pass in a path to a json file or give the list instead. The concept is that you don't need to touch the code if you have to change some recurring tasks (if you use json).
# How to install  
There are no extra modules needed. You can copy the filecreator folder to your project.
# Quick Usage
To use this small module you can import it, initialize and run. The example can be found in the main.py file.
```python
from filecreator import FileCreator
data = [
    {"filename": "Myfile.txt", "path": [], "default": "Default MyFile"},
    {"filename": "MyOtherFile.txt", "path": ["testfoler"], "default": "Default OtherFile"}
]

# Initialize
creator = FileCreator("files.json", data)
# run the creator
creator.run()
```
This will create the requested files in the requested directories.
# FileCreator class
The class has the following parameters when you create an instance of the class:<br />
<i>filecreator.FileCreator(json_path:str=None, data:List=None)</i>
<ul><li><strong>json_path</strong>: Default=None - The path to the json file as a string (I recommend the os module with os.path.join() if it is deeper in the filesystem).</li>
<li><strong>data</strong>: Default=None - If you already have the data, you can provide it here as a list of dictonaries.</li>
<li><strong>json_key</strong>: Default=None - Key where the JSON file contains the filelist as a string.</li>
<li><strong>json_position</strong>: Default=0 - Integer position where JSON file contains the filelist. If nothing is provided at the key it will take the first position, but you can pass a higher position if nessesary (see JSON Format for more information).</li></ul>
If json_path and data have values they will be merged together. The order is json_path->data.


# Format
Each list entry is a dictonary. The structure needs to be the following:
```python
data = [
    {"filename": "Myfile.txt", "path": [], "default": "Default MyFile"},
    {"filename": "MyOtherFile.txt", "path": ["testfolder"], "default": "Default OtherFile"}
]
```
<ul><li><strong>filename</strong> is the name of the file.</li>
<li><strong>path</strong> is the path where the file needs to be located. It is a list with folders. If the tree does not exist it will be created. If the file has to be created in the same directory, you pass an empty list.</li>
<li><strong>default</strong> is the content of the file. It can be left empty if no default is needed.</li></ul>

# JSON Format
The JSON file has to look like this:
```json
{
    "data": [
        {"filename": "file1.txt", "path": ["testfolder", "testfolder2"], "default": "This is the default of File 1" },
        {"filename": "file2.txt", "path": ["testfolder"], "default": "" }
        ]
}
```
The filecreator class picks the first entry (here "data") as default. You can pass a specific key (param: json_key: string) or the position number (param: json_position: integer). 