# Function & Class Reference
This document explains the main classes used in the Digital Art Archive Management System and what each one does.


## Module: `artwork.py`
### Class: `Artwork`
Represents one artwork in the archive. It stores the artist, title, year, type of artwork, and image path.

**Key Features**
- Fixes and formats artist names.
- Makes sure the year is valid (0–2025).
- Checks the artwork type (Painting, Photograph, Sculpture, Drawing).
- Can check if the image file meets minimum resolution.

**Important Properties**
- `artist`  
- `title`  
- `year`  
- `art_type`  
- `image_path`  

## Module: `Artwork_record_manager.py`
### Class: `ArtworkRecordManager`
Creates a validated artwork record with a unique ID. This is mainly for metadata, not images.

**Validations**
- Title and artist must not be empty.
- Year must be between 1000–2025.
- Type must be: Painting, Sculpture, or Photograph.

**Main Methods**
- `to_dict()` → returns the artwork record as a dictionary.
- `get_age()` → shows how old the artwork is.
- Automatically creates an ID based on the title + artist + year digits.

**Read-Only Properties**
- `title`
- `artist`
- `year`
- `art_type`
- `artwork_id`

## Module: `ArtCollection.py`
### Class: `ArtCollection`
Stores multiple artworks inside a named collection.

**Main Features**
- Cleans the collection name.
- Allows you to add artworks with optional dimensions and value.
- Can remove artworks by title.
- Can search by artist name.
- Calculates total value of the collection.

**Properties**
- `name`
- `artworks` (read-only list)
- `total_value()` (calculated)

## Module: `user_management_project3.py`
### Class: `AbstractUser`
Base class for all types of users in the system.

Each user has:
- an ID  
- a name  
- an email  
- a list of borrowed artworks  

Users must define:
- How many items they can borrow  
- What access level they have  

Users can borrow artworks using:
- `borrow_artwork(artwork)`

### User Types
#### `StudentUser`
- Borrowing limit: **3**
- Access level: **Basic Access**

#### `ResearcherUser`
- Borrowing limit: **10**
- Access level: **Premium Access**

#### `CuratorUser`
- Borrowing limit: **999**
- Access level: **Gold Access**

### Class: `UserRegistry`
Manages all users in the system.

**Main Methods**
- `register_user(user)` → adds a new user  
- `display_all_users()` → shows a summary of users  
- `get_users_by_type(type)` → filters users by type  

This document is meant to help developers understand how each major class works.
