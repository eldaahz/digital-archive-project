## Class: Artwork_Record - Faith C.

Represents an artwork record in the digital archive collection with focus on metadata validation, searching, and temporal analysis.

### Main Attributes
- **_title** (str): Title of the artwork  
- **_artist** (str): Artist’s name  
- **_year** (int): Year created (1000–2025)  
- **_art_type** (str): Type of artwork  
- **_keywords** (list): Optional keywords for tagging  

### Class Variable
- **VALID_TYPES** (list): List of allowed artwork types  

### Key Methods
- **__init__()** – Creates an artwork and checks that all info is valid  
- **_validate_year()** – Makes sure the year is within the correct range  
- **is_from_period()** – Checks if the artwork was made between two years  
- **to_dict()** – Turns the artwork info into a dictionary  
- **get_age()** – Finds how old the artwork is  
- **__str__() / __repr__()** – Returns readable text versions of the artwork
