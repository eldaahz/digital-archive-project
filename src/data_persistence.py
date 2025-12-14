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
            "type": doc.__class__.__name__,
            "title": artwork._title,
            "artist": artwork._artist,
            "year": artwork._year
        }
        
        # Add specific attributes
        if hasattr(doc, 'pages'):
            doc_data['pages'] = doc.pages
        elif hasattr(doc, 'issue_number'):
            doc_data['issue_number'] = doc.issue_number
        elif hasattr(doc, 'recipient'):
            doc_data['recipient'] = doc.recipient
        elif hasattr(doc, 'scale'):
            doc_data['scale'] = doc.scale
        elif hasattr(doc, '_art_type'):
            doc_data['art_type'] = doc._art_type
        
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
            if hasattr(doc, '_art_type'):
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
            if start_year <= doc.year <= end_year:
                doc_type = getattr(doc, '_art_type', doc.__class__.__name__)
                writer.writerow([artwork._title, artwork._artist, artwork._year, artwork._art_type])

#Demo
if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    
    from artwork_record import Artwork
    
    artwork1 = Artwork("Starry Night", "Van Gogh", 1889, "Painting")
    artwork2 = Artwork("Mona Lisa", "Da Vinci", 1503, "Painting")
    
    print("=== Created Artworks ===")
    print(artwork1)
    print(artwork2)
    
    print("\n=== CSV Import Demo ===")
    print("import_artworks_csv() can load artworks from CSV files")
    print("export_artworks_csv() can save collections to CSV")

