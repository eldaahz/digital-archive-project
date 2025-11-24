## Artwork Record Class - Faith C.

**Purpose:** Represents artwork records in the digital archive with focus on metadata validation and time-based analysis.

**Key Design Decisions:**

1. **Encapsulation:** I used private attributes (`_title`, `_artist`, `_year`, `_art_type`) with `@property` decorators to make sure the data can't be changed after the artwork is created for information accuracy.

2. **Project 1 Integration:**
   - `_validate_year()` - integrates my validate_year() function (enforces 1000-2025 range)
   - `is_from_period()` - adapts my find_art_by_year_range() for single artwork queries
   - `get_age()` - calculates artwork age for time analysis
   - `to_dict()` - converts artwork to dictionary format for compatibility with Project 1 functions

**Read-only Properties:** I made title, artist, year, and art_type read-only because once an artwork is created, its core metadata shouldn't change for accuracy.

## Artwork Class - Atena Nikbakht

**Purpose:** Represents an individual artwork in the collection that stores key metadata such as the artist, title, year, type, and image. Class integrates Project 1 functions to ensure validation, standardization, and image quality.

**Key Design Decisions:**
1. **Encapsulation:** Used private attributes (_artist, _title, _year, _type, _image_path) with @property decorators to ensure controlled access.

2. **Project 1 Integration:**
- _standardize_artist_name() – integrates my standardize_artist_name() function to clean and format artist names.
- _validate_year() – adapts my validate_year() logic to ensure valid numeric range (0–2025).
- artwork_type() – incorporates my artwork_type() function to validate artwork categories.
- validate_image_resolution() – applies my validate_image_resolution() function to verify image file quality.

**Read-only Properties:** Title, year, art_type, and image_path are read-only after intiialization
to maintain record consistency and maintain integrity.

## Artwork Collection Class - Eldaah Z
**Purpose**: This represents managing and analyzing multiple artworks instead of individual metadata. This class integrate Project 1 functions.

**Key Design Decisions**: 
1.) **Encapsulation** I used private attributes like _collection_name and _artworks to prevent direct modification from the outside class and force users to use controlled methods like .add_work() or .remove_artwork()
2.) **Project 1 Integration**: 
- validate_dimenstions() - ask user for heigh, length, & width while ensuring positive numbers are entered
- clean_titles() - remove special characters and extra whitespace from artwork titles
- search_art_by_artist() - ask for artist input and displays work from the artist

## ArtworkRecordManager Class – Selamawit Asmare 

**Purpose:** 
Validates and manages artwork records in the Digital Art Archive.
It ensures each entry has valid metadata and a unique ID for accurate storage.

*Key Design:*
1. Compile: Used private attributes (_title, _artist, _year, _art_type, _artwork_id) with @property decorators to protect data integrity.
2. Project 1 Integration:
       _parse_creation_year() adapts parse_creation_year() to validate year range.
       _generate_artwork_id() integrates generate_artwork_id() for auto ID creation.
       to_dict() builds on validate_artwork_record() for formatted record output.
3. Read-only Properties: Title, artist, year, and type are read-only after initialization to maintain accuracy.

## User Management System (Faith Chang)

Inheritance: AbstractUser is the parent class with three types of users. Each user type "is a" user.

Composition: UserRegistry "has" users inside it.

Polymorphism: Same method gives different results - students get 3, researchers get 10, curators get 999.



