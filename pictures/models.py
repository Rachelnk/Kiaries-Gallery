from email.mime import image
from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class Location (models.Model):
    name = models.CharField(max_length=60)

    def __str__ (self):
      return self.name

    @classmethod
    def get_all_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod
    def update_location(cls, id, value ):
      cls.objects.filter(id=id).update(location=value)     

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
        

    

class Categories (models.Model):
    name = models.CharField (max_length=60)
    
    def save_category(self):
      self.save()

    def delete_category(self):
      self.delete()

    def __str__ (self):
      return self.name

class Image (models.Model):
  image = models.ImageField(upload_to = 'images/')
  name = models.CharField(max_length =60)
  description = models.TextField()
  uploadby = models.CharField(max_length= 60, default='admin')
  author = models.CharField(max_length = 60)
  pub_date = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Categories, on_delete= models.CASCADE)
  location = models.ForeignKey (Location, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def save_image(self):
      self.save()

  def delete_image(self):
      self.delete()
  @classmethod
  def get_all_images(cls):
      all_images = Image.objects.all()
      return all_images

  @classmethod
  def get_image(cls, id):
    image = cls.objects.filter(id=id).all()
    return image

  @classmethod
  def update_image(cls, id, value ):
    cls.objects.filter(id=id).update(image=value)

  @classmethod
  def filter_by_location(cls, location):
      image_location = Image.objects.filter(location__name__icontains= location)
      return image_location
  @classmethod
  def search_by_category(cls, search_term):
    images = cls.objects.filter(category__name__icontains=search_term)
    return images

  class Meta:
    ordering = ['pub_date']


