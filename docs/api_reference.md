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

## Class: Artwork - Atena Nikbakht
Represents an individual artwork in the collection that stores key metadata such as the artist, title, year, type, and image. Class integrates Project 1 functions to ensure validation, standardization, and image quality.

### Main Attributes
- _artist (str): Name of the artist, standardized for consistency.
- _title (str): Title of the artwork.
- _year (int): Year the artwork was created (validated between 0–2025).
- _type (str): Artwork type (e.g., Painting, Photograph, Sculpture, Drawing).
- _image_path (str): File path to the artwork image for validation and display.

### Key Methods:
- __init__() – Initializes an artwork object, validating all inputs upon creation.
- _standardize_artist_name(name) – Formats artist names consistently (e.g., “Doe, John” → “John Doe”).
- artwork_type(art_type) – Validates the artwork type against accepted categories.
- _validate_year(year) – Ensures the year is an integer within the valid range.
- validate_image_resolution(min_width, min_height) – Checks that the image file meets minimum resolution requirements.
- __str__() / __repr__() – Provide readable and formal text representations of the artwork for printing and debugging.

### Class - ArtCollection - Eldaah Z.
This represents managing and analyzing multiple artworks instead of individual metadata. This class integrate Project 1 functions. 

## Main Attributes
- _artworks = [] : list of available artworks 

## Key Methods: 
- __init__() : initializes an empty collection of artworks
- add_artwork(artwork) : adds and artwork object to the collection (by title + artist)
- search_by_artisit(artist_name) : searches the collection for artworks by specific artwork
- filter_by_dimensions(min_height=0, min_length=0, min_width=0) : returns artwork that meet or exceed the specified dimensions
- list_titles() : returns a list of all artwork titles in the collection


