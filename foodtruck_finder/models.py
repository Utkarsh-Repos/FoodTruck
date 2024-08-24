from django.db import models

class FoodTruck(models.Model):
    applicant = models.CharField(max_length=500)
    facility_type = models.CharField(max_length=50)
    location_description = models.CharField(max_length=1000)
    address = models.CharField(max_length=255)
    food_items = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.applicant
