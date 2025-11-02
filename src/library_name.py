from datetime import datetime

class ArtworkRecordManager:
    """
    Represents a manager for validating, creating, and organizing artwork records
    in the digital art archive system.

    Integrates Project 1 functions:
    - generate_artwork_id()
    - parse_creation_year()
    - validate_artwork_record()

    Attributes:
        _artwork_id (str): Unique artwork ID.
        _title (str): Artwork title.
        _artist (str): Artist name.
        _year (int): Year created (1000–2025).
        _art_type (str): Artwork category.
    """
  
    VALID_TYPES = ["Painting", "Sculpture", "Photograph"]

    def __init__(self, title: str, artist: str, year: int, art_type: str):
        """Initialize and validate an artwork record."""
        self._title = self._validate_text(title, "title")
        self._artist = self._validate_text(artist, "artist")
        self._year = self._parse_creation_year(year)
        self._art_type = self._validate_art_type(art_type)
        self._artwork_id = self._generate_artwork_id()

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def year(self):
        return self._year

    @property
    def art_type(self):
        return self._art_type

    @property
    def artwork_id(self):
        return self._artwork_id

    def _validate_text(self, value: str, field: str) -> str:
        """Validate non-empty text input."""
        if not value or not value.strip():
            raise ValueError(f"{field.capitalize()} cannot be empty.")
        return value.strip().title()

    def _parse_creation_year(self, year: int) -> int:
        """Validate year range (1000–2025)."""
        try:
            year = int(year)
        except ValueError:
            raise ValueError("Year must be a number.")
        if year < 1000 or year > 2025:
            raise ValueError("Year must be between 1000 and 2025.")
        return year

    def _validate_art_type(self, art_type: str) -> str:
        """Ensure artwork type is one of the allowed types."""
        art_type = art_type.strip().capitalize()
        if art_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid artwork type. Choose from {', '.join(self.VALID_TYPES)}.")
        return art_type

    def _generate_artwork_id(self) -> str:
        """Generate a simple unique ID based on title and artist."""
        short_title = self._title[:3].upper()
        short_artist = self._artist[:3].upper()
        year_suffix = str(self._year)[-2:]
        return f"{short_title}{short_artist}{year_suffix}"

    def to_dict(self):
        """Return artwork info in dictionary format."""
        return {
            "ID": self._artwork_id,
            "Title": self._title,
            "Artist": self._artist,
            "Year": self._year,
            "Type": self._art_type
        }

    def get_age(self):
        """Return how old the artwork is in years."""
        return datetime.now().year - self._year

    def __str__(self):
        return f"[{self._artwork_id}] {self._title} by {self._artist} ({self._year}) - {self._art_type}"

    def __repr__(self):
        return f"ArtworkRecordManager({self._title!r}, {self._artist!r}, {self._year!r}, {self._art_type!r})"

if __name__ == "__main__":
    artwork = ArtworkRecordManager("Starry Night", "Vincent van Gogh", 1889, "Painting")
    print(artwork)
    print("Dictionary:", artwork.to_dict())
    print("Artwork age:", artwork.get_age(), "years")
