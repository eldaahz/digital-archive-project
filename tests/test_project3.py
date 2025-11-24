# Selma - Project 3

import unittest
import sys


sys.path.append('src')

from artwork_record import Artwork
from user_management_project3 import AbstractUser, StudentUser, ResearcherUser, CuratorUser, UserRegistry
class TestAbstractClasses(unittest.TestCase):
    """Test the abstract classes they cannot be instantiated."""
    
    def test_cannot_instantiate_abstract_user(self):
        with self.assertRaises(TypeError):
            AbstractUser("MONET001", "Luna Sanchez", "luna@impressionism.org")

class TestInheritance(unittest.TestCase):
    """Test inheritance relationships."""
    
    def test_student_inherits(self):
        student = StudentUser("PICASSO42", "Daisy Mai", "daisy@cubism.edu", "Modern Art History")
        self.assertIsInstance(student, AbstractUser)
    
    def test_all_users_inherit(self):
        users = [
            ResearcherUser("FRIDA88", "Robert Senai", "robert@surrealism.edu", "Mexican Muralism"),
            CuratorUser("VANGOGH7", "Senai Luna", "senai@postimpressionism.org", "Dutch Masters")
        ]
        for user in users:
            self.assertIsInstance(user, AbstractUser)

class TestPolymorphism(unittest.TestCase):
    """Test polymorphic behavior."""
    
    def test_different_borrowing_limits(self):
        users = [
            StudentUser("WARHOL10", "Mai Robert", "mai@popart.edu", "Contemporary Photography"),
            ResearcherUser("KLIMT23", "Luna Daisy", "luna@artnouveau.edu", "Symbolist Painting"),
            CuratorUser("DALI99", "Daisy Senai", "daisy@surrealism.org", "Abstract Expressionism")
        ]
        limits = [u.calculate_borrowing_limit() for u in users]
        self.assertEqual(limits, [3, 10, 999])

class TestComposition(unittest.TestCase):
    """Test composition relationships."""
    
    def test_registry_contains_users(self):
        registry = UserRegistry("Guggenheim Digital Archive")
        user = StudentUser("MATISSE5", "Robert Luna", "robert@fauvism.edu", "Color Theory")
        registry.register_user(user)
        self.assertIn(user, registry.users)

class TestSuperUsage(unittest.TestCase):
    """Test super() calls work properly."""
    
    def test_student_has_parent_attributes(self):
        student = StudentUser("MONET3", "Senai Mai", "senai@impressionism.edu", "Landscape Studies")
        self.assertEqual(student._user_id, "MONET3")
        self.assertEqual(student._name, "Senai Mai")

class TestIntegrationWithArtwork(unittest.TestCase):
    """Test that User system integrates with existing Artwork classes."""
    
    def test_user_can_borrow_artwork(self):
        student = StudentUser("REMBRANDT8", "Luna Robert", "luna@baroque.edu", "Dutch Golden Age")
        artwork = Artwork("The Starry Night", "Vincent van Gogh", 1889, "Painting")
        self.assertTrue(student.borrow_artwork(artwork))

if __name__ == '__main__':
    unittest.main()