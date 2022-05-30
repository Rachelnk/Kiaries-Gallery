from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index , name = 'index'),
  path('search/', views.search_results, name = 'search'),
  re_path('^location/(?P<location>\w+)/$', views.image_location, name = 'location' ),
  path('gallery/', views.gallery, name = 'gallery')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)