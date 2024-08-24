from math import radians, cos, degrees


def calculate_bounding_box(lat, lon, radius):
    # Radius of Earth in kilometers
    earth_radius = 6371

    # Angular distance in radians
    angular_distance = radius / earth_radius

    # Calculate latitude and longitude bounds
    min_lat = lat - degrees(angular_distance)
    max_lat = lat + degrees(angular_distance)
    min_lon = lon - degrees(angular_distance / cos(radians(lat)))
    max_lon = lon + degrees(angular_distance / cos(radians(lat)))

    return min_lat, max_lat, min_lon, max_lon