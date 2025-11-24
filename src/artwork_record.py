#Faith - Class 
class Artwork:
  """Represents an artwork in the digital archive collection"""
  VALID_TYPES = ["Painting", "Sculpture", "Photograph", "Digital Art", "Drawing", "Mixed Media"]
  def __init__(self, title, artist, year, art_type , keywords = None):
    """Start an artwork with validation
    Args:
      title (str): The artwork's title
      artist (str): The artist's name
      year (int): Year created (1000-2025)
      art_type (str): Type of artwork
     keywords (list): Optional keywords
    Raises:
       ValueError: If parameters are invalid
    """
    if not title or not title.strip():
      raise ValueError("Title should not be empty")
    if not artist or not artist.strip():
      raise ValueError(f"Artist name should not be empty")
    if art_type not in self.VALID_TYPES:
      raise ValueError(f"Invalid artwork type")
  
    self._title = title.strip()
    self._artist = artist.strip()
    self._year = self._validate_year(year)
    self._art_type = art_type
    self._keywords = keywords if keywords else []

  @property
  def year(self):
    """int: Get creation year"""
    return self._year
  @property
  def artist(self):
      """str: Get the artist name."""
      return self._artist

  @property
  def art_type(self):
      """str: Get the artwork type."""
      return self._art_type
      
  def _validate_year(self, year):
      """Validate year between 1000-2025 (Integration from Project 1)."""
      try:
        year_num = int(year)
        if 1000 <= year_num <= 2025:
          return year_num
        raise ValueError("Year should be between 1000 and 2025")
      except (ValueError, TypeError):
        raise ValueError("Invalid year")

  def is_from_period(self, start_year, end_year):
      """Check if the artwork is within a time period (Integration from Project 1).
      Returns:
        bool: True if it is within range
      """
      if start_year > end_year:
        raise ValueError("Invalid year range")
      return start_year <=self._year <= end_year

  def to_dict(self):
    """Convert artwork to dictionary format for data processing.
    
    Returns dictionary format compatible with Project 1 functions.
    
    Returns:
        dict: Dictionary with 'title', 'artist', 'year', 'type' keys
    """
    return {
        "title": self._title,
        "artist": self._artist,
        "year": self._year,
        "type": self._art_type
    }

  def get_age(self):
    """Calculate how old the artwork is (Integration from Project 1).
    
    Returns:
        int: Age of the artwork in years
    """
    from datetime import datetime
    current_year = datetime.now().year
    return current_year - self._year

  def __str__(self):
      return f"{self._title} by {self._artist} ({self._year}) - {self._art_type}"
  def __repr__(self):
      return f"Artwork({self._title!r}, {self.artist!r}, {self._year})"

#Test 
artwork_1 = Artwork("Starry Night", "Vincent van Gogh", 1889, "Painting")
print(artwork_1)
print(f"Is artwork from 1880-1990? {artwork_1.is_from_period(1880, 1990)}")
print(f"Dictionary format: {artwork_1.to_dict()}")
print(f"Artwork age: {artwork_1.get_age()} years old")

