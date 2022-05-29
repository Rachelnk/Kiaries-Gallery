from django.contrib import admin
from .models import Categories, Image, Location

# Register your models here.
admin.site.register(Image)
admin.site.register(Categories)
admin.site.register(Location)

