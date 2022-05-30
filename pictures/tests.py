from django.test import TestCase
from .models import Categories, Location, Image

# Create your tests here.
class CategoriesTestClass(TestCase):

    def setUp(self):
        self.category = Categories(name = 'food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food)), Categories

    def test_save_method(self):
        self.category.save_category()
        categories = Categories.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Categories.objects.all()
        self.assertTrue(len(category) == 0)

class LocationTestCase(TestCase):
    def setUp(self):
        self.category = Categories(name = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi)), Location

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_all_locations()
        self.assertTrue(len(locations) > 1)

    def test_update_location(self):
        new_location = 'Nairobi'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='Nairobi')
        self.assertTrue(len(changed_location) > 0)


    def tearDown(self):
        Categories.objects.all().delete()
        Location.objects.all().delete()

    
        
