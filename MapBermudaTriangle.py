import folium

# Coordinates of the vertices of the Bermuda Triangle
bermuda_triangle_coords = [
    (25.7617, -80.1918),  # Miami, Florida
    (18.4655, -66.1057),  # San Juan, Puerto Rico
    (32.3078, -64.7505)   # Bermuda
]

# Create a map centered around the midpoint of the Bermuda Triangle
center_lat = sum([lat for lat, lon in bermuda_triangle_coords]) / len(bermuda_triangle_coords)
center_lon = sum([lon for lat, lon in bermuda_triangle_coords]) / len(bermuda_triangle_coords)
mymap = folium.Map(location=[center_lat, center_lon], zoom_start=5)

# Add markers for each vertex
for lat, lon in bermuda_triangle_coords:
    folium.Marker([lat, lon], popup=f'Lat: {lat}, Lon: {lon}').add_to(mymap)

# Add a polygon to represent the Bermuda Triangle
folium.Polygon(
    locations=bermuda_triangle_coords,
    color='blue',
    weight=2,
    fill=True,
    fill_color='blue',
    fill_opacity=0.2
).add_to(mymap)

# Save the map to an HTML file
mymap.save('bermuda_triangle.html')

print("Map has been created and saved as 'bermuda_triangle_map.html'")
