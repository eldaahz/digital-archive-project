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
