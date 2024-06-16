import pandas as pd
from geopy.geocoders import Nominatim
import folium
from folium.plugins import HeatMap

# Step 1: Load your CSV data
# Replace 'your_file.csv' with your actual CSV file path
df = pd.read_csv('zip_codes.csv')

# Ensure your CSV has a column named 'zip_code' or modify accordingly
zip_codes = df['zip_code'].tolist()

# Step 2: Geocode the zip codes to get latitudes and longitudes
geolocator = Nominatim(user_agent="zip_code_locator")
locations = []

for zip_code in zip_codes:
    try:
        location = geolocator.geocode({"postalcode": zip_code, "countryRegion": "United States"})
        if location:
            locations.append((location.latitude, location.longitude))
    except:
        pass

# Step 3: Create a base map
map_center = [37.0902, -95.7129]  # Center of the US
heat_map = folium.Map(location=map_center, zoom_start=5)

# Step 4: Add heat map layer
HeatMap(locations).add_to(heat_map)

# Step 5: Save the map to an HTML file
heat_map.save('zip_code _heatmap.html')