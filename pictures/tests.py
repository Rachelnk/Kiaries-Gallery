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

    def tearDown(self):
        Categories.objects.all().delete()

    def test_delete_category(self):
        self.category.delete_category()
        category = Categories.objects.all()
        self.assertTrue(len(category) == 0)
        
