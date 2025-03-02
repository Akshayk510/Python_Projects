
import folium
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_geocoder_app")
address = input("Enter an address to map: ")

location = geolocator.geocode(address)
if location:
    lat,lon = location.latitude, location.longitude
else:
    print("Address not found. Defaulting to white House.")
    lat, lon = 38.8976524,-77.036591
    
m = folium.Map(location=[lat, lon],zoom_start=15)
folium.Marker(
    loaction=[lat, lon],
    popup=f"{address}",
    icon=folium.Icon(color="blue")).add_to(m)

m.save("map.html")
