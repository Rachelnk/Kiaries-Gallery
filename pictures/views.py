from email.mime import image
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Image, Location

# Create your views here.
def index(request):
  images = Image.objects.all()
  locations = Location.get_all_locations()
  print(locations)
  return render (request, 'all-photos/index.html')

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(searched_images)
        return render(request, 'all-photos/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'all-photos/search_results.html', {"message": message})

def image_location (request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render (request, 'all-photos/location.html', {'location_image': images})





