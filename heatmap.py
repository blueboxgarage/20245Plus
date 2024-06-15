import pandas as pd
import plotly.express as px
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Photon

geolocator = Photon(user_agent="measurements")

df = pd.read_csv('zip_codes.csv', sep='\t', header=None, index_col=False, names=['zipcode'])


# Function to get latitude and longitude
def get_lat_long(zipcode):
    try:
        location = geolocator.geocode(zipcode)
        return location.latitude, location.longitude
    except (AttributeError, GeocoderTimedOut):
        return None, None


# Create new columns for latitude and longitude
df[['latitude', 'longitude']] = df['zipcode'].apply(lambda x: pd.Series(get_lat_long(x)))

# Drop rows with missing values
# df = df.dropna(subset=['latitude', 'longitude'])

# Count occurrences of each zip code
# df['count'] = df.groupby('zip_code')['zip_code'].transform('count')

# Remove duplicates
# df = df.drop_duplicates(subset=['zip_code'])

# Plot the heat map using Plotly
# fig = px.density_mapbox(df, lat='latitude', lon='longitude', z='count', radius=10,
#                       center=dict(lat=37.0902, lon=-95.7129), zoom=3,
#                      mapbox_style="stamen-terrain", title="Heat Map of Credit Card Applicants")

fig = px.choropleth(df,
                    geojson=df,
                    locations='zip_code',
                    featureidkey="properties.ZCTA5CE10",
                    color='value',
                    color_continuous_scale="blues",
                    projection="mercator",
                    )

# Show the heat map
fig.show()
