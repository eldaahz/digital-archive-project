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
