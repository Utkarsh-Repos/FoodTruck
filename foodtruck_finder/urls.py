from django.urls import path, include

urlpatterns = [
    path("foodtruck_finder/", include('foodtruck_finder.api.urls')),
]