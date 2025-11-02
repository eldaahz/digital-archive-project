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
