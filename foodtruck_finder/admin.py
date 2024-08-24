from django.contrib import admin
from .models import FoodTruck


class FoodTruckAdmin(admin.ModelAdmin):
    pass

admin.site.register(FoodTruck, FoodTruckAdmin)