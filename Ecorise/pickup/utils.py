from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_coordinates(location_name, retries=3):
    geolocator = Nominatim(user_agent="ecorise")
    for attempt in range(retries):
        try:
            location = geolocator.geocode(location_name)
            if location:
                return location.latitude, location.longitude
        except GeocoderTimedOut:
            if attempt == retries - 1:
                break 
    return None, None
