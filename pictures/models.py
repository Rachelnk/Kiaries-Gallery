from statistics import mode
from django.db import models

# Create your models here.
class location (models.Model):
    name = models.CharField(max_length=60)
class Image (models.Model):
  image = models.ImageField(upload_to = 'images/')
  name = models.CharField(max_length =60)
  description = models.TextField()
  uploadby = models.CharField(max_length= 60, default='admin')
  # author = models.ForeignKey(Editor)
  pub_date = models.DateTimeField(auto_now_add=True)
  

