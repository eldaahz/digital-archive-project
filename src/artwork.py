#Atena Class
from PIL import Image

class Artwork:
  """
  This class represents an artwork in the collection which stores different metadata such as the artist, year, type, and image file based on previous funcitons made.
  Previous functions being used:
  - standardize_artist_name(name:str):
  - validate_image_resolution(file_path: str, min_width: int, min_height: int):
  - artwork_type(art_type: str):
  - search_art_by_metadata(artworks: list, search_term: str, search_field: str = "all"):
  """
  def __init__(self, artist: str, title: str, year: int, art_type: str, image_path:str):
    # Using previous functions to
    self._artist = self._standardize_artist_name(artist)
    self._title = title.strip().title()
    self._year = self._validate_year(year)
    self._type = self.artwork_type(art_type)
    self._image_path = image_path

  #Properties for encapsulation
  @property
  def artist(self):
    return self._artist

  @artist.setter
  def artist(self, value):
    self._artist = self._standardize_artist_name(value)

  @property
  def title(self):
    return self._title

  @property
  def year(self):
    return self._year

  @property
  def art_type(self):
    return self._type

  @property
  def image_path(self):
    return self._image_path


  def _standardize_artist_name(self, name: str):
    if not name or not isinstance(name, str):
      raise ValueError("Invalid artist name.")
    name = name.strip()
    if "," in name:
      parts = name.split(",", 1)
      name = parts[1].strip() + " " +parts[0].strip()
    name = " ".join(name.split())
    return name.title()

  def artwork_type(self, art_type: str):
    valid_types = {
        "painting": "Painting",
        "photograph": "Photograph",
        "sculpture": "Sculpture",
        "drawing": "Drawing",
    }
    art_type = art_type.strip().lower()
    if art_type not in valid_types:
      raise ValueError(f"Unknown or invalid artwork type '{art_type}'. Please choose from: {', '.join(valid_types.values())}.")
    return valid_types[art_type]

  def _validate_year(self, year: int):
    if not isinstance(year, int) or year <0 or year > 2025:
      raise ValueError("Invalid year for artwork.")
    return year

  def validate_image_resolution(self, min_width: int, min_height: int):
    try:
      with Image.open(self._image_path) as img:
        width, height = img.size
      if width >= min_width and height >= min_height:
        return True
      else:
        return False
    except FileNotFoundError:
      raise FileNotFoundError("Image file was not found.")
    except Exception as e:
      raise ValueError("Error reading image file.") from e

  def __str__(self):
    return f"Artwork(title = '{self.title}', artist = '{self._artist}', type = '{self._type}', year = {self._year})"

  def __repr__(self):
    return f"Artwork({self.artist!r}, {self._title!r}, {self._year!r}, {self._type!r}, {self._image_path!r})"

