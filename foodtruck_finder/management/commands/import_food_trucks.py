import csv
from django.core.management.base import BaseCommand
from foodtruck_finder.models import FoodTruck


class Command(BaseCommand):
    """
    Import food truck data from a CSV file into the FoodTruck table.
    """

    def handle(self, *args, **kwargs):
        with open("foodtruck_finder/static/food-truck-data.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                FoodTruck.objects.create(
                    applicant=row["Applicant"],
                    facility_type=row["FacilityType"],
                    location_description=row["LocationDescription"],
                    address=row["Address"],
                    food_items=row["FoodItems"],
                    latitude=float(row["Latitude"]),
                    longitude=float(row["Longitude"]),
                )
        self.stdout.write(self.style.SUCCESS("Data imported successfully!"))
