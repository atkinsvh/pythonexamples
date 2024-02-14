import pandas as pd
from geopy.geocoders import Nominatim
import folium
from folium.plugins import HeatMap
from pyscript import document

# Load the DataFrame from the CSV file
df = pd.read_csv('output.csv')

# Create a map centered at a specific location
m = folium.Map(location=[40.0, -80.0], zoom_start=6)  # You can adjust the center and zoom level

# Ensure the coordinates are not NaN
df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

# Convert data to list of tuples
locations = df[['Latitude', 'Longitude']].values.tolist()

# Add heatmap layer
HeatMap(locations).add_to(m)

# m.save('/Users/djentwistle/Desktop/ExamplesPyscript/Test/heatmap.html')

# display(m, target="folium")


# Create a div element to contain the map
map_div = document.createElement("div")
map_div.id = "map"  # Set the id attribute for styling or manipulation

