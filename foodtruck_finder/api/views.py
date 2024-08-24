from math import radians, cos, sin, sqrt, atan2
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from foodtruck_finder.models import FoodTruck
from .serializers import FoodTruckSerializer
from .helpers import calculate_bounding_box


class FoodTruckListView(APIView):
    """
    Returns food trucks within a specified radius of a given location.

    Query Parameters:
    - latitude (float): Latitude of the center.
    - longitude (float): Longitude of the center.
    - radius (float, optional): Radius in km (default is 1 km).

    Responses:
    - 200 OK: List of food trucks within the radius.
    - 400 Bad Request: Invalid latitude or longitude.
    """
    def get(self, request, *args, **kwargs):
        """
       Get food trucks within the specified radius from given latitude and longitude.

       Returns:
           Response: JSON list of nearby food trucks or error message.
       """
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        radius = request.query_params.get('radius', 1)

        if latitude and longitude:
            try:
                latitude = float(latitude)
                longitude = float(longitude)
            except ValueError:
                return Response({'error': 'Invalid latitude or longitude'}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate bounding box
        min_lat, max_lat, min_lon, max_lon = calculate_bounding_box(latitude, longitude, float(radius))

        food_trucks = FoodTruck.objects.filter(
            latitude__gte=min_lat,
            latitude__lte=max_lat,
            longitude__gte=min_lon,
            longitude__lte=max_lon
        )

        nearby_trucks = []
        for truck in food_trucks:
            distance = self.haversine_distance(latitude, longitude, truck.latitude, truck.longitude)
            if float(distance) <= float(radius):
                nearby_trucks.append((truck, distance))

        # Sort by distance and take the nearest 5 trucks
        nearby_trucks.sort(key=lambda x: x[1])
        nearest_trucks = [truck for truck, _ in nearby_trucks[:5]]

        serializer = FoodTruckSerializer(nearest_trucks, many=True)
        return Response(serializer.data)


    @staticmethod
    def haversine_distance(lat1, lon1, lat2, lon2):
        """
        Compute the distance between two geographic points using the Haversine formula.

        Args:
            lat1 (float): Latitude of the first point.
            lon1 (float): Longitude of the first point.
            lat2 (float): Latitude of the second point.
            lon2 (float): Longitude of the second point.

        Returns:
            float: Distance in kilometers.
        """

        # Converts latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        r = 6371  # Radius of Earth in kilometers
        return r * c