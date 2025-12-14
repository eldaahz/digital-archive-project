#Faith Chang - Project 4
import json
import csv
from pathlib import Path
from datetime import datetime

def save_collection(art_archive, filename):
    """Save art archive to JSON file."""
    filepath = Path(filename)
    
    data = {
        "name": art_archive.name,
        "saved_at": datetime.now().isoformat(),
        "documents": []
    }
    
    for artwork in art_archive.documents:
        doc_data = {
            "type": artwork.__class__.__name__,
            "title": artwork._title,
            "artist": artwork._artist,
            "year": artwork._year
        }
        
        
        data["documents"].append(doc_data)
    
    with filepath.open('w') as f:
        json.dump(data, f, indent=2)

def load_collection(filename):
    """Load art archive from JSON file."""
    filepath = Path(filename)
    
    if not filepath.exists():
        raise FileNotFoundError(f"Archive file '{filename}' not found. Save your collection first!")
    
    with filepath.open('r') as f:
        return json.load(f)

def import_artworks_csv(filename):
    """Import artworks from CSV (format: title,artist,year,type)."""
    filepath = Path(filename)
    
    if not filepath.exists():
        raise FileNotFoundError(f"Artwork CSV file '{filename}' not found. Check the file path!")
    
    artworks = []
    with filepath.open('r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            artworks.append({
                'title': row['title'],
                'artist': row['artist'],
                'year': int(row['year']),
                'type': row['type']
            })
    return artworks

def export_artworks_csv(collection, filename):
    """Export all artworks to CSV."""
    filepath = Path(filename)
    
    with filepath.open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'artist', 'year', 'type'])
        
        for artwork in collection.documents:
                writer.writerow([artwork._title, artwork._artist, artwork._year, artwork._art_type])

def export_period_report(collection, start_year, end_year, filename):
    """Export artworks from time period to CSV."""
    if start_year > end_year:
        raise ValueError(f"Invalid period: {start_year} must be before {end_year}")
    
    filepath = Path(filename)
    
    with filepath.open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'creator', 'year', 'type'])
        
        for artwork in collection.documents:
            if start_year <= artwork._year <= end_year:
                writer.writerow([artwork._title, artwork._artist, artwork._year, artwork._art_type])

# Demo 
if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    
    from artwork_record import Artwork
    
    # Create test collection
    class DemoCollection:
        def __init__(self, name):
            self.name = name
            self.documents = []
        def add_document(self, doc):
            self.documents.append(doc)
    
    archive = DemoCollection("Digital Art Archive")
    archive.add_document(Artwork("Starry Night", "Van Gogh", 1889, "Painting"))
    archive.add_document(Artwork("Mona Lisa", "Da Vinci", 1503, "Painting"))
    
    print("=== Saving Archive ===")
    save_collection(archive, "demo_archive.json")
    print("Saved to demo_archive.json")
    
    print("\n=== Loading Archive ===")
    data = load_collection("demo_archive.json")
    print(f"Loaded: {data['name']} with {len(data['documents'])} artworks")

