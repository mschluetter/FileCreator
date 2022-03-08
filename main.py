from filecreator import FileCreator

def main() -> None:
    data = [
        {"filename": "Myfile.txt", "path": [], "default": "Default MyFile"},
        {"filename": "MyOtherFile.txt", "path": ["testfolder"], "default": "Default OtherFile"}
    ]

    creator = FileCreator("files.json", data)
    creator.run()

if __name__=="__main__":
    main()