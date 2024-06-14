import unittest
import datetime
from models.BaseModel import BaseModel
from models.Place import Place
from models.Country import Country
from models.City import City
from models.Amenities import Amenities
from models.User import User
from models.Review import Review

class TestModels(unittest.TestCase):

    def setup_tests(self):
        self.user = User(email="user@example.com", password="supersecretpassword", name="John Doe")
        self.amenity = Amenities()
        self.amenity.name = "Kitchen"
        self.amenity.description = "Small Kitchen"

        self.city = City()
        self.city.name = "Paris"
        
        self.country = Country()
        self.country.name = "France"
        
        self.place = Place(owner=self.user.id, address="123 Road", description="Cool place with cool stuff", price="200", city=self.city.id, pictures=[])
        
        self.review = Review()
        self.review.note = "I loved the place and the landscape!"
        self.review.rating = 5

    def constistency_tests(self):
        now = datetime.datetime.now()
        self.assertIsInstance(self.user.createdAt, datetime.datetime)
        self.assertIsInstance(self.user.updatedAt, datetime.datetime)
        
        old_updatedAt = self.user.updatedAt
        self.user.name = "Jane Doe"
        self.user.save()
        
        self.assertNotEqual(old_updatedAt, self.user.updatedAt)
        self.assertGreater(self.user.updatedAt, old_updatedAt)
    
    def integrity_tests(self):
        self.place.owner = self.user.id
        self.assertEqual(self.place.owner, self.user.id)
        
        self.review.placeID = self.place.id
        self.review.client = self.user.id
        
        self.assertEqual(self.review.placeID, self.place.id)
        self.assertEqual(self.review.client, self.user.id)
    
    def enforcement_tests(self):
        another_user = User(email="secondary@example.com", password="supersecretpassword", name="Jane Doe")
        
        with self.assertRaises(ValueError):
            another_place = Place(name="Another Place", description="Another nice place", owner=another_user.id)
            self.place.owner = another_user.id
            self.place.save()
    
    def validation_tests(self):
        with self.assertRaises(ValueError):
            invalid_user = User(email="random_fake_email", password="supersecretpassword", name = "John Doe")
        
        with self.assertRaises(ValueError):
            invalid_user = User(email="", password="supersecretpassword", name = "John Doe")
    
    def unique_tests(self):
        with self.assertRaises(ValueError):
            duplicate_user = User(email="user@example.com", password="supersecretpassword", name = "Jane Doe")
    
    def mechanism_tests(self):
        self.user.name = "Jane Doe"
        self.user.save()
        
        updated_user = User(email="user@example.com")
        self.assertEqual(updated_user.name, "Jane Doe")
    
    def instantiation_tests(self):
        with self.assertRaises(ValueError):
            invalid_place = Place(name="", description="Another nice place", owner=self.user.id)
        
        valid_place = Place(name="A Correct Place", description="Another nice place", owner=self.user.id)
        valid_place.save()
    
    def assignment_tests(self):
        new_host = User(email="new_email@example.com", password="supersecretpassword", name = "New User")
        new_host.save()
        
        self.place.user_id = new_host.id
        self.place.save()
        
        self.assertEqual(self.place.user_id, new_host.id)
    
    def att_validation_tests(self):
        with self.assertRaises(ValueError):
            self.place.latitude = 200.0
            self.place.save()
        
        with self.assertRaises(ValueError):
            self.place.price_per_night = -100.0
            self.place.save()
    
    def deleting_tests(self):
        place_id = self.place.id
        self.place.delete()
        
        with self.assertRaises(ValueError):
            Place.get(place_id)
    
    def amenities_tests(self):
        amenity_id = self.amenity.id
        self.amenity.name = "Updated WiFi"
        self.amenity.save()
        
        updated_amenity = Amenities.get(amenity_id)
        self.assertEqual(updated_amenity.name, "Updated WiFi")

if __name__ == '__main__':
    unittest.main()