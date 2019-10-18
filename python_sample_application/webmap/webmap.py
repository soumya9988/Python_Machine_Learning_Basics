import folium
import pandas as pd

map_f = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles= "Stamen Terrain")

fg = folium.FeatureGroup(name='Test Map')

data = pd.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
# elev1 = data.iloc[:, 5].values
# print(elev)
# print(elev1)

elev_info = """ <h5>Volcano information:</h5>
                Height: %s m """
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup= elev_info % str(el), icon=folium.Icon(color='red')))
    map_f.add_child(fg)


map_f.save('check_map.html')