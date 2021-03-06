from django.test import TestCase
from .models import Categories, Location, Image

# Create your tests here.
class CategoriesTestClass(TestCase):

    def setUp(self):
        self.category = Categories(name = 'food')

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Categories))

    def test_save_method(self):
        self.category.save_category()
        categories = Categories.objects.all()
        self.assertTrue(len(categories) > 0)    

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)


    # def test_get_locations(self):
    #     self.location.save_location()
    #     locations = Location.get_all_locations()
    #     self.assertTrue(len(locations) > 1)

    def test_update_location(self):
        new_location = 'Nairobi'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='Nairobi')
        self.assertTrue(len(changed_location) > 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

        self.category = Categories(name='food')
        self.category.save_category()

        self.image_test = Image(id=1, name='image', description='test image', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='Nairobi')
        self.assertTrue(len(found_images) == 1)

    # def test_search_image_by_category(self):
    #     category = 'food'
    #     found_img = self.image_test.search_by_category(category)
    #     self.assertTrue(len(found_img) > 1)

    def tearDown(self):
        Categories.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    
        
