from django.urls import path, include
from .views import fetch_truck_data


urlpatterns = [
    path("foodtruck_finder/", include('foodtruck_finder.api.urls')),
    path("", fetch_truck_data),

]