import unittest
from filecreator import FileCreator

class TestFileCreator(unittest.TestCase):
    
    def test_from_file(self):
        creator = FileCreator("files.json")
        self.assertEqual(len(creator.data), 1)

if __name__ == "__main__":
    unittest.main()