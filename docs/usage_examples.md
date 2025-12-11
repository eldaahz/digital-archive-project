# Usage Examples (Simplified)

These examples show how to use the main parts of the Digital Art Archive System.  
Before running, make sure Python can find the `src` folder:

```python
import sys
sys.path.append("src")

1. Creating a Validated Artwork Record
python
Copy code
from Artwork_record_manager import ArtworkRecordManager

record = ArtworkRecordManager(
    "Starry Night",
    "Van Gogh, Vincent",
    1889,
    "Painting"
)

print(record)
print(record.to_dict())
print("Age:", record.get_age())
2. Creating an Artwork with an Image
python
Copy code
from artwork import Artwork

art = Artwork(
    "Van Gogh, Vincent",
    "Starry Night",
    1889,
    "Painting",
    "images/starry_night.jpg"
)

print(art)
print("Image quality OK?", art.validate_image_resolution(800, 600))
3. Adding Artworks to a Collection
python
Copy code
from artwork import Artwork
from ArtCollection import ArtCollection

collection = ArtCollection("Impressionist Favorites")

art1 = Artwork("Van Gogh, Vincent", "Starry Night", 1889, "Painting", "img1.jpg")
art2 = Artwork("Claude Monet", "Water Lilies", 1899, "Painting", "img2.jpg")

dims1 = {"Height": 73, "Length": 92, "Width": 5}
dims2 = {"Height": 100, "Length": 81, "Width": 4}

collection.add_artwork(art1, dims1, value=1_000_000)
collection.add_artwork(art2, dims2, value=800_000)

print("Total value:", collection.total_value())
4. Searching by Artist
python
Copy code
results = collection.search_by_artist("Van Gogh, Vincent")

for item in results:
    print(item["artwork"].title, "-", item["artwork"].artist)
5. Registering Users and Borrowing Artworks
python
Copy code
from user_management_project3 import UserRegistry, StudentUser
from artwork import Artwork

registry = UserRegistry("UMD Digital Archive")

student = StudentUser("STU001", "Alex Rivera", "alex@umd.edu", "Info Science")
registry.register_user(student)

art = Artwork("Van Gogh, Vincent", "Starry Night", 1889, "Painting", "img1.jpg")

print("Borrow success?", student.borrow_artwork(art))

for info in registry.display_all_users():
    print(info)
These examples show the typical workflow of the system:
create artwork → add to collection → register users → allow borrowing.

