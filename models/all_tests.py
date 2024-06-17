import unittest
import datetime
import os
import sys
from BaseModel import BaseModel
from City import City
from Place import Place
from Country import Country
from Amenity import Amenity
from User import User
from Review import Review
current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)
from persistence.DataManager import DataManager

dm = DataManager()

class TestModels(unittest.TestCase):

    def setUp(self):
        User.emails = set()
        self.user = User(email="supertest@example.com", password="password", first_name="John", last_name="Doe")
        self.amenity = Amenity()
        self.amenity.name = "WiFi"
        self.amenity.description = "Free WiFi"
        
        self.city = City()
        self.city.name = "San Francisco"
        self.city.population = 1000000
        self.city.user_id = self.user.id
        
        self.country = Country()
        self.country.name = "USA"
        self.country.population = 330000000
        self.country.city_id = [self.city.id]
        
        self.place = Place(name="Test Place", description="A nice place", address="123 Main St", longitude=-122.4194, latitude=37.7749, price_per_night=100.0, number_of_rooms=3, bathrooms=2, max_guests=6, amenity_id=(self.amenity.id,), city_id=self.city.id, host_id=self.user.id)
        
        self.review = Review()
        self.review.feedback = "Great place!"
        self.review.rating = 5
        self.review.comment = "Had a wonderful time."

    def test_consistency_checks(self):
        now = datetime.datetime.now()
        
        old_updatedAt = self.user.updatedAt
        self.user.first_name = "Jane"
        dm.update(self.user)
        new_user = dm.get(self.user.id, "User")
    
    def test_relationship_integrity(self):
        self.place.user_id = self.user.id
        self.assertEqual(self.place.user_id, self.user.id)
        
        self.review.place = self.place.id
        self.review.user = self.user.id
        
        self.assertEqual(self.review.place, self.place.id)
        self.assertEqual(self.review.user, self.user.id)
    
    def test_user_creation_validation(self):
        with self.assertRaises(ValueError):
            invalid_user = User(email="invalid_email", password="password", first_name="John", last_name="Doe")
        
        with self.assertRaises(ValueError):
            invalid_user = User(email="", password="password", first_name="John", last_name="Doe")
    
    def test_place_instantiation(self):
        with self.assertRaises(ValueError):
            invalid_place = Place(name="", description="Description", address="123 Main St", longitude=-122.4194, latitude=37.7749, price_per_night=100.0, number_of_rooms=3, bathrooms=2, max_guests=6)
        
        valid_place = Place(name="Valid Place", description="Description", address="123 Main St", longitude=-122.4194, latitude=37.7749, price_per_night=100.0, number_of_rooms=3, bathrooms=2, max_guests=6)
        dm.save(valid_place)
    
    def test_host_assignment_rules(self):
        new_host = User(email="newhost@example.com", password="password", first_name="New", last_name="Host")
        dm.save(new_host)
        
        self.place.user_id = new_host.id
        dm.save(self.place)
        
        self.assertEqual(self.place.user_id, new_host.id)
    
    def test_deleting_places(self):
        place_id = self.place.id
        dm.delete(self.place, "Place")

        self.assertEqual(dm.get(place_id, "Place"), None)
            
    

if __name__ == '__main__':
    unittest.main()