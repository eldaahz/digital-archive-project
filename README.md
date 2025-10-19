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

# Team Member Contributions

**Atena Nikbakht** - Search by metadata function
**Eldaah Zelalem** - 
**Faith Chang*** - 

