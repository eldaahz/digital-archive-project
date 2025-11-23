from abc import ABC, abstractmethod

# Abstract Base Class
class AbstractDocument(ABC):
    def __init__(self, title, creator, year):
        self.title = title
        self.creator = creator
        self.year = year

    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def preservation_instructions(self):
        pass

# Derived Classes
class Manuscript(AbstractDocument):
    def __init__(self, title, creator, year, pages):
        super().__init__(title, creator, year)
        self.pages = pages

    def display_info(self):
        return f"[Manuscript] {self.title} by {self.creator} ({self.year}) — {self.pages} pages"

    def preservation_instructions(self):
        return "Keep in acid-free folder at 20°C, 50% humidity"

class Newspaper(AbstractDocument):
    def __init__(self, title, creator, year, issue_number):
        super().__init__(title, creator, year)
        self.issue_number = issue_number

    def display_info(self):
        return f"[Newspaper] {self.title} by {self.creator} ({self.year}) — Issue {self.issue_number}"

    def preservation_instructions(self):
        return "Store flat, avoid sunlight, digitize ASAP"

class Letter(AbstractDocument):
    def __init__(self, title, creator, year, recipient):
        super().__init__(title, creator, year)
        self.recipient = recipient

    def display_info(self):
        return f"[Letter] {self.title} from {self.creator} to {self.recipient} ({self.year})"

    def preservation_instructions(self):
        return "Keep in archival sleeve, low light"

class Map(AbstractDocument):
    def __init__(self, title, creator, year, scale):
        super().__init__(title, creator, year)
        self.scale = scale

    def display_info(self):
        return f"[Map] {self.title} by {self.creator} ({self.year}) — Scale 1:{self.scale}"

    def preservation_instructions(self):
        return "Roll loosely, store in tube, avoid moisture"

# Composition: Archive Collection
class ArchiveCollection:
    def __init__(self, name):
        self.name = name
        self.documents = []

    def add_document(self, doc: AbstractDocument):
        self.documents.append(doc)

    def display_all(self):
        return [doc.display_info() for doc in self.documents]

    def preservation_guide(self):
        return [f"{doc.title}: {doc.preservation_instructions()}" for doc in self.documents]

# Demo
if __name__ == "__main__":
    archive = ArchiveCollection("Historical Archive")
    archive.add_document(Manuscript("Shakespeare's Sonnets", "Shakespeare", 1609, 154))
    archive.add_document(Newspaper("The Times", "London Times", 1820, 12))
    archive.add_document(Letter("Letter to Lincoln", "Frederick Douglass", 1863, "Abraham Lincoln"))
    archive.add_document(Map("Map of Paris", "Cartographer A", 1789, 50000))

    print("=== All Documents ===")
    for info in archive.display_all():
        print(info)

    print("\n=== Preservation Instructions ===")
    for guide in archive.preservation_guide():
        print(guide)
