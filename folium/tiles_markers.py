import folium


m = folium.Map(location=[-19.5736261, -44.0365116],  zoom_start=5,
               tiles='Stamen Terrain')

# gerencias tiles
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('stamentoner').add_to(m)
folium.TileLayer('stamenterrain').add_to(m)
folium.TileLayer('stamenterrain').add_to(m)
folium.TileLayer('Mapbox Control Room').add_to(m)
folium.LayerControl().add_to(m)

# add long e lat click
m.add_child(folium.LatLngPopup())

# add marker click
m.add_child(folium.ClickForMarker(popup="Waypoint"))

m.save('mapa_index.html')
