from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class Location (models.Model):
    name = models.CharField(max_length=60)

    def __str__ (self):
      return self.name

class Categories (models.Model):
    name = models.CharField (max_length=60)

    def __str__ (self):
      return self.name

class Image (models.Model):
  image = models.ImageField(upload_to = 'images/')
  name = models.CharField(max_length =60)
  description = models.TextField()
  uploadby = models.CharField(max_length= 60, default='admin')
  author = models.CharField(max_Length = 60)
  pub_date = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Categories)
  location = models.ForeignKey (Location)

  def __str__(self):
    return self.name
  

