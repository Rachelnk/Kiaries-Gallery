from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Image, Location

# Create your views here.
def index(request):
  images = Image.objects.all()


  return render (request, 'all-photos/index.html')


