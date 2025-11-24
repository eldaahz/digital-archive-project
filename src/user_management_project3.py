# Faith - Project 3
from abc import ABC, abstractmethod


class AbstractUser(ABC):
    """Base class for all archive system users."""
    
    def __init__(self, user_id, name, email):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._borrowed_artworks = []
    
    @property
    def user_id(self):
        return self._user_id
    
    @abstractmethod
    def calculate_borrowing_limit(self):
        """Max artworks this user can borrow."""
        pass
    
    @abstractmethod
    def get_access_level(self):
        """Return user's access privileges."""
        pass
    def borrow_artwork(self, artwork):
        """Borrow an artwork from the collection."""
        if len(self._borrowed_artworks) < self.calculate_borrowing_limit():
            self._borrowed_artworks.append(artwork)
            return True
        return False


class StudentUser(AbstractUser):
    def __init__(self, user_id, name, email, major):
        super().__init__(user_id, name, email)
        self.major = major
    
    def calculate_borrowing_limit(self):
        return 3
    
    def get_access_level(self):
        return "Basic Access"

class ResearcherUser(AbstractUser):
    def __init__(self, user_id, name, email, field):
        super().__init__(user_id, name, email)
        self.field = field
    
    def calculate_borrowing_limit(self):
        return 10
    
    def get_access_level(self):
        return "Premium Access"

class CuratorUser(AbstractUser):
    def __init__(self, user_id, name, email, department):
        super().__init__(user_id, name, email)
        self.department = department
    
    def calculate_borrowing_limit(self):
        return 999
    
    def get_access_level(self):
        return "Gold Access"


class UserRegistry:
    """Manages all users in the archive system."""
    
    def __init__(self, institution_name):
        self.institution_name = institution_name
        self.users = []
    
    def register_user(self, user: AbstractUser):
        self.users.append(user)
    
    def display_all_users(self):
        return [f"{u._name} - {u.get_access_level()} (Limit: {u.calculate_borrowing_limit()})" 
                for u in self.users]
    
    def get_users_by_type(self, user_type):
        return [u for u in self.users if isinstance(u, user_type)]


if __name__ == "__main__":
    registry = UserRegistry("MoMA Digital Collection Archive")
    
    registry.register_user(StudentUser("PICASSO15", "Luna Sanchez", "luna@cubism.edu", "Cubist Sculpture Studies"))
    registry.register_user(ResearcherUser("FRIDA88", "Robert Mai", "robert@surrealism.edu", "Latin American Muralism"))
    registry.register_user(CuratorUser("WARHOL42", "Daisy Senai", "daisy@popart.org", "Contemporary Pop Art"))
    
    print("=== All Users ===")
    for info in registry.display_all_users():
        print(info)