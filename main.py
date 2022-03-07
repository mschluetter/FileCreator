from filecreator import FileCreator

def main() -> None:
    creator = FileCreator("files.json")
    creator.run()

if __name__=="__main__":
    main()