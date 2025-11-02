# Digital Art Archive Management System

#We are building an archive management system meant for cataloging, searching, and managing digital collections specific to art. We will integrate metadata standards and an object-oriented system in order to apply the program to multiple different archive formats. 

# Team members and roles:
#Faith Chang - User Experience Designer

#Eldaah Zelalem - Documentation Manager

#Atena Nikbakht – Project Coordinator

#Selamawit Asmare - Researcher

# The problem:
It can be complicated to keep track of art and the different artists, including their creation dates, types of art, etc. Creating an archive management system to organize, manage, and search this information can make art collections easier to store. Organizations such as Universities can benefit from this system. 

# Installation and Setup
1. Open Google Colab or VS Code.
2. Copy and paste the function code from our GitHub repository into a new Python file.
3. Save and run the file to test each function.
4. In Google Colab, click the Play button beside each cell to run it.

# Usage examples for key functions
1. def artwork_type(art_type: str):
  This function will organize artworks into their respective categories. Like if it is a painting or a sculpture.
2. search_art_by_artist()
   This function prompts the user to enter an artist's name and prints their artwork if any is found
3. def standardize_artist_name(name:str)
 This function will standardize the given artist name so we can compare all names and store them. It will be in a "Last Name, First Name" format. This function will remove whitespace and fix capitalization
4. validate_image_resolution(file_path: str, min_width: int, min_height: int)
   This function ensures that the images added to the system fit the resolution requirements for the best quality.
5. search_art_by_metadata
   This function allows the user to search through the system using different metadata, such as the artist, artwork title, or year created. The return value is the number of matches found with the keywords given.

# Function library overview and organization
Our function library is organized by complexity level and team member contributions to make it easy to read and test. 

Each team member contributed 3–5 functions showing their understanding of:
Function definition and syntax
User input handling
Conditional logic and validation
Data storage using dictionaries

Together, these functions make up the Digital Art Archive Management System, which will later evolve into a more advanced, object-oriented program capable of managing and searching large collections of digital artworks.


# Team Member Contributions

**Atena Nikbakht** - Search by metadata function
**Eldaah Zelalem** - 
**Faith Chang** - Artwork type storage and Validation
**Selamawit Asmare** - Data Validation and record management functions

# Classes
**Artwork - Faith Chang**
Represents an individual artwork in the digital archive collection.

*Features*
- Validates artwork data (title, artist, year (1000-2025), type)
- Integrates functions from Project 1
- Searches artwork by the artist, title, year, or different keywords
- Checks if artwork is from a specific time period

*Properties*
- 'title', 'artist', 'year', 

*Methods*
- 'is_from_period()' -> Checks if artowrk is created within the date range
- 'matches_search() -> Searches by various field
- 'add_keyword()' -> Adds metadata keywords
