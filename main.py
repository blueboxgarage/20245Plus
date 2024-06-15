import pandas as pd
from geopy.geocoders import GoogleV3
import gmplot

# Replace 'YOUR_GOOGLE_API_KEY' with your actual Google API key
google_api_key = 'AIzaSyBAl7YsNqJ5BTJuW6dFINOaGWrF1CY2Bhk'

# Initialize the geolocator with your Google API key
geolocator = GoogleV3(api_key=google_api_key)

# Read the ZIP codes from the CSV file
zip_codes_df = pd.read_csv('zip_codes.csv')

# List to hold the latitude and longitude coordinates
coordinates = []

# Geocode each ZIP code to get the coordinates
for zip_code in zip_codes_df['zip_code']:
    try:
        location = geolocator.geocode(zip_code)
        if location:
            coordinates.append((location.latitude, location.longitude))
    except Exception as e:
        print(f"Error geocoding ZIP code {zip_code}: {e}")

# Ensure there are valid coordinates to plot
if coordinates:
    # Extract the latitude and longitude values
    latitudes, longitudes = zip(*coordinates)

    # Create the GoogleMapPlotter object centered around the first ZIP code's coordinates
    gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 5)

    # Create a heatmap on the GoogleMapPlotter object
    gmap.heatmap(latitudes, longitudes)

    # Save the map to an HTML file
    gmap.draw("heatmap.html")
    print("Heatmap has been created and saved as 'heatmap.html'.")
else:
    print("No valid coordinates to plot.")