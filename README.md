# Digital Art Archive Management System

#We are building an archive management system meant for cataloging, searching, and managing digital collections specific to art. We will integrate metadata standards and an object-oriented system in order to apply the program to multiple different archive formats. 

# Team members and roles:
   #Faith Chang - User Experience Designer

   #Eldaah Zelalem - Documentation Manager

   #Atena Nikbakht – Project Coordinator

   #Selamawit Asmare - Researcher

# The problem:
It can be complicated to keep track of art and the different artists, including their creation dates, types of art, etc. Creating an archive management system to organize, manage, and search this information can make art collections easier to store. Organizations such as Universities can benefit from this system. 

# Installation and Setup
1. Clone this repository:
```bash
   git clone https://github.com/eldaahz/digital-archive-project.git
   cd art-archive-system
```
2. No external dependencies required - uses Python standard library only

3. Import functions in your Python code:
```python from src.archive_library import search_art_by_metadata, validate_dimensions
``` 

# Installation and Setup
1. Open Google Colab or VS Code.
2. Copy and paste the function code from our GitHub repository into a new Python file.
3. Save and run the file to test each function.
4. In Google Colab, click the Play button beside each cell to run it.

# Usage examples for key functions
###Cataloging artwork
'''python
from src.archive_library import validate_dimension, ststandardize_artist_name
dimensions = validate_dimensions()
clean_name = standarized_artist_name("van gogh, vincent")

### Searching archive
'''python
from src.archive_library import search_art_by_metadata
artworks = [
    {"title": "Starry Night", "artist": "Vincent van Gogh", "year": 1889, "type": "Painting", "keywords": ["post-impressionism", "night", "stars"]},
    {"title": "Water Lilies", "artist": "Claude Monet", "year": 1899, "type": "Painting", "keywords": ["impressionism", "light", "French"]}
]
results = search_art_by_metadata(artworks, "Monet", "artist")
'''

### Data validation
'''python
from src.archive_library import parse_creation_year, validate_artwork_record
year = parse_creation_year()
record = validate_artwork_record()
'''

# Function library overview and organization

Our function library is organized by complexity level and team member contributions to make it easy to read and test. 

Each team member contributed 3–5 functions showing their understanding of:
Function definition and syntax
User input handling
Conditional logic and validation
Data storage using dictionaries

Together, these functions make up the Digital Art Archive Management System, which will later evolve into a more advanced, object-oriented program capable of managing and searching large collections of digital artworks.


# Team Member Contributions

**Atena Nikbakht** - Search by metadata function
**Eldaah Zelalem** - User retrieval & search functionality 
**Faith Chang** - Artwork type storage and Validation
**Selamawit Asmare** - Data Validation and record management functions

# Classes

**Artwork Record - Faith Chang**
Represents an artwork record in the digital archive collection that focuses on metadata, searching, and time analysis.

*Features*
- Validates artwork data (title, artist, year (1000-2025), type)
- Integrates functions from Project 1
- Analyzes time properties such as age and time periods
- Exports dictionary format for data processing

*Properties*
- 'title', 'artist', 'year', 'art_type' 

*Methods*
- 'is_from_period()' -> Checks if artowrk is created within the date range
- 'to_dict() -> Converts dictionary format that is compatible from Project 1 functions
- 'get_age()' -> Calculates how old the artwork is in years

**Artwork Record Manager – Selamawit Asmare**

*Purpose:*
Validates and manages artwork records in the Digital Art Archive. It checks input data, creates unique IDs, and keeps records consistent.

Uses private attributes (_title, _artist, _year, _art_type, _artwork_id) with read-only properties to protect data.

*Integration:*
_parse_creation_year() checks valid year range.
_generate_artwork_id() creates short unique IDs.
to_dict() reformats data for earlier validation functions.

*Key Methods:*
_validate_text(), _validate_art_type(), _generate_artwork_id(), get_age(), and to_dict().

*Design Note:* Supports accurate data entry and future inheritance.

** Artwork - Atena Nikbakht**
This class represents a single artwork within the system and records metadata such as the artist, title, year, type, and image.

*Features*
- Initializes a new artwork object and validates/standardizes all inputs (artist, title, year, type, image).
- Cleans up artist name and puts it in Last Name, First Name, format
- Checks that given artwork type falls into an accepted category
- Verifies that artwork meets width and height criteria

Properties: artist, title, year, art_type, image_path

Methods:
- Constructor (__init__)
- 5 property accessors
- 3 internal validation methods
- 2 string methods
- 


# Project 3
AbstractDocument Hierarchy:
Purpose: To store and manage physical archives.

AbstractDocument (ABC)
│
├── Manuscript
│     └─ Attributes: pages
│     └─ Methods: display_info(), preservation_instructions()
│
├── Newspaper
│     └─ Attributes: issue_number
│     └─ Methods: display_info(), preservation_instructions()
│
├── Letter
│     └─ Attributes: recipient
│     └─ Methods: display_info(), preservation_instructions()
│
└── Map
      └─ Attributes: scale
      └─ Methods: display_info(), preservation_instructions()

Composition:
ArchiveCollection
└─ Contains: multiple AbstractDocument objects
   └─ Methods: add_document(), display_all(), preservation_guide()

## Key features:
display_info() → Abstract method; shows a description of the document.

preservation_instructions() → Abstract method; provides guidelines for preserving the document.


## Purpose: Manages users and how many artworks they can borrow.

AbstractUser (ABC)
- StudentUser: Can borrow 3 artworks, Basic Access
- ResearcherUser: Can borrow 10 artworks, Premium Access  
- CuratorUser: Can borrow 999 artworks, Gold Access

Composition:
UserRegistry holds multiple users

Key features:
calculate_borrowing_limit() - Each user type has different borrowing limits.
get_access_level() - Each user type has different access levels.


### OOP Concepts

1. Encapsulation -- Our system protects the interval state of the programing by keeping attributes private and exposing only safe public methods.
Example:
class ArchiveItem:
    def __init__(self, title, creator, year):
        self._title = title          # private
        self._creator = creator      # private
        self._year = year            # private

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value

2. Inheritance -- Our project defines a parent class ArchiveItem and child classes that extend it.
Example:
class ImageItem(ArchiveItem):
    def __init__(self, title, creator, year, resolution):
        super().__init__(title, creator, year)
        self.resolution = resolution

3. Polymorphism -- This system implements the same method differently for each item type.
Example:
class ArchiveItem(ABC):
    @abstractmethod
    def summarize(self):
        pass

class ImageItem(ArchiveItem):
    def summarize(self):
        return f"Image: {self.title} ({self.year})"

class DocumentItem(ArchiveItem):
    def summarize(self):
        return f"Document: {self.title} — {self.creator}"

4. Abstract Base Classes -- Foundational base classes are implemented that cannot be instantiated but enforced required mehtods.
Example:
from abc import ABC, abstractmethod

class ArchiveItem(ABC):

    @abstractmethod


    def summarize(self):
        pass

# Project 4
Overview - 

Managing art collections can be complex when tracking multiple artists, artworks, and locations. This system provides a structured way to store this information, answer questions about the collection, and maintain data across sessions.This document covers the three completeness tests that verify the Art Archive Management System answers all charter questions and functions correctly end-to-end.

Test 1 - Which artist has the most artworks? 

Purpose: Verify the system identitfies the most prolific artist correctly 
Example: 
def test_artist_question_1_complete(self):
    archive = ArtArchive()
    
    # Add artworks: Picasso (2), Monet (1)
    archive.add_artwork(title="Work 1", creator="Picasso", date="1920",
                       type="Painting", format="Oil on canvas")
    archive.add_artwork(title="Work 2", creator="Picasso", date="1921",
                       type="Painting", format="Oil on canvas")
    archive.add_artwork(title="Work 3", creator="Monet", date="1890",
                       type="Painting", format="Oil on canvas")
    
    result = archive.get_proflific_artist()
    
    self.assertIsNotNone(result)
    self.assertEqual(result['creator'], "Picasso")
    self.assertEqual(result['count'], 2)

Expected: Picasso identified with 2 artworks

Test 2 - Is file format supported?

Purpose: Verfiy JPG, PNG, and TIFF formats are supported and unsupported formats are rejected.
Example: 
def test_supported_file_formats(self):
    archive = ArtArchive()
    
    # Supported formats
    self.assertTrue(archive.validate_file_format("image.jpg"))
    self.assertTrue(archive.validate_file_format("image.jpeg"))
    self.assertTrue(archive.validate_file_format("image.png"))
    self.assertTrue(archive.validate_file_format("image.tiff"))
    self.assertTrue(archive.validate_file_format("image.tif"))
    
    # Unsupported format
    with self.assertRaises(ValueError):
        archive.validate_file_format("image.gif")
Expected: JPG/PNG/TIFF pass; GIF raises ValueError

Test 3 - Complete User Workflow 

Purpose: Test entire system workflow from import to export
Example: 
def test_complete_workflow(self):
    # Create admin user and archive
    admin = User("admin@museum.edu", role="admin")
    archive = ArtArchive(current_user=admin)
    
    # Import, add, tag, save, load, export
    count = archive.import_from_csv("museum_collection.csv")
    archive.add_artwork(title="New Acquisition", creator="Contemporary Artist",
                       date="2024", type="Digital Art", format="Digital print",
                       file_format="PNG")
    archive.add_tag_to_artwork("New Acquisition", "Contemporary")
    
    archive.save("complete_archive.json")
    loaded = ArtArchive.load("complete_archive.json", current_user=admin)
    loaded.generate_report("collection_report.txt")
    loaded.export_to_csv("collection_export.csv")
    
    # Verify
    self.assertEqual(len(loaded.artworks), count + 1)
    self.assertTrue(Path("collection_report.txt").exists())
    self.assertTrue(Path("collection_export.csv").exists())
    
Expected: All operations succeed; data persists correctly.

