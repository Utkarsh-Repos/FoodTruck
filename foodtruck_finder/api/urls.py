from django.urls import path
from .views import FoodTruckListView


urlpatterns = [
    path('finder/', FoodTruckListView.as_view(), name='finder'),
]