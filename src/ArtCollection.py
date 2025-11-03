from datetime import datetime 

class ArtCollection: 
  """ 
  Represents a collection of artworks within a museum or archive. 

  Attributes (private): 
  _name (str): Name of the collection 
  _artworks (list): Stores Artwork objects
  _created_at (datetime): Timestamp when the collection was created

  Read-Only Properties: 
    name (str): Collection name 
    artworks (tuple): Safe, read-only version of artworks list
    created_at (datetime): When the colelction was initialized
    total_value (float): Combined value of all artworks 
  """

def __init__(self,name): 
  self._name = self._clean_collection_name(name)
  self._artworks = []
  self._created_at = datetime.now()

def _clean_collection_name(self,name): 
  """Uses clean_titles from project 1"""
  special =  r"!@#$%^&*()+-_\/?<>~`:;[]{}"
  for symbol in special: 
    name = name.replace(symbol, "")
  return name.strip().title()

def _validate_dimensions(self, dimensions): 
  """Uses validate_dimensions()from project 1""" 
  if not isinstance(dimensions, dict): 
    raise ValueError("Dimensions must be a dictionary with Height, Length, and Width")
  for key in ["Height", "Length", "Width"]: 
    if key not in dimensions or dimensions[key] <= 0: 
      raise ValueError("All dimensions must be positive numbers")

    return dimensions
                     
def add_artwork(self, artwork, dimensions=None, value=0.0):
  """
  Adds an artwork to the collection with optional dimensions and value.
  """
  if dimensions:
                     self._validate_dimensions(dimensions)
                     artwork_info = {
                         "artwork": artwork, 
                         "dimensions": dimensions, 
                         "value": float(value)
                     }
                     self._artworks.appen(artwork_info)
def remove_artwork(self, title): 
  """Removes an artwork by title if it exists."""
  for art in self._artworks: 
    if art["artwork"].title.lower() == title.lower():
    self._artworks.remove(art)
    return True 
    return False
def search_by_artist(self, artist_name): 
  """Simulates Project 1 search_art_by_artist() functionality."""
  return [
      art for art in self._artworks
      if art["artwork"].artist.lower() == artist_name.lower()
  ]

@property 
def name(self):
  return self.__name

@property
def artworks(self):
  """Returns a safe, read-only version of artworks list"""
  return tuple(self._artworks)

def total_value(self):
  """Automatically sums the value of all artworks"""
  return sum(art["value"] for art in self._artworks)

def __str__(self): 
  return f"ArtCollection(name='{self._name}', artworks={len(self._artworks)})"

def __repr__(self): 
  return f"ArtCollection(name='{self._name}', created_at={self._created_at})"
                   
