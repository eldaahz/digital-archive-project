#Faith Chang - Project 4
import unittest
import json
import csv
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from data_persistence import *
from artwork_record import Artwork

class TestCollection:
    def __init__(self, name):
        self.name = name
        self.documents = []
    
    def add_document(self, doc):
        self.documents.append(doc)

class TestPersistence(unittest.TestCase):
    
    def setUp(self):
        self.archive = TestCollection("Digital Art Archive")
        self.archive.add_document(Artwork("Starry Night", "Van Gogh", 1889, "Painting"))
        self.archive.add_document(Artwork("Mona Lisa", "Da Vinci", 1503, "Painting"))
        self.archive.add_document(Artwork("David", "Michelangelo", 1504, "Sculpture"))
        
        self.json_file = Path("test.json")
        self.csv_file = Path("test.csv")
    
    def tearDown(self):
        if self.json_file.exists():
            self.json_file.unlink()
        if self.csv_file.exists():
            self.csv_file.unlink()
    
    def test_save_creates_file(self):
        save_collection(self.archive, str(self.json_file))
        self.assertTrue(self.json_file.exists())
    
    def test_save_valid_json(self):
        save_collection(self.archive, str(self.json_file))
        with self.json_file.open('r') as f:
            data = json.load(f)
        self.assertEqual(data['name'], "Digital Art Archive")
        self.assertEqual(len(data['documents']), 3)
    
    def test_load_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            load_collection("missing.json")
    
    def test_load_returns_data(self):
        save_collection(self.archive, str(self.json_file))
        data = load_collection(str(self.json_file))
        self.assertEqual(data['name'], "Digital Art Archive")
    
    def test_import_missing_csv(self):
        with self.assertRaises(FileNotFoundError):
            import_artworks_csv("missing.csv")
    
    def test_export_creates_csv(self):
        export_artworks_csv(self.archive, str(self.csv_file))
        self.assertTrue(self.csv_file.exists())
    
    def test_period_invalid_range(self):
        with self.assertRaises(ValueError):
            export_period_report(self.archive, 2000, 1000, str(self.csv_file))
    
    def test_save_load_roundtrip(self):
        save_collection(self.archive, str(self.json_file))
        data = load_collection(str(self.json_file))
        self.assertEqual(len(data['documents']), 3)
    
    def test_csv_workflow(self):
        with self.csv_file.open('w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['title', 'artist', 'year', 'type'])
            writer.writerow(['The Girl with a Pearl Earring', 'Johannes Vermeer', '1666', 'Painting'])
        
        artworks = import_artworks_csv(str(self.csv_file))
        self.assertEqual(len(artworks), 1)
        self.assertEqual(artworks[0]['title'], 'The Girl with a Pearl Earring')
    
    def test_complete_workflow(self):
        save_collection(self.archive, str(self.json_file))
        data = load_collection(str(self.json_file))
        export_period_report(self.archive, 1500, 1900, str(self.csv_file))
        
        with self.csv_file.open('r') as f:
            rows = list(csv.reader(f))
        self.assertEqual(len(rows), 4) 

if __name__ == '__main__':
    unittest.main()
