import folium
import pandas as pd


def colour_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'blue'
    else:
        return 'red'


data = pd.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
# elev1 = data.iloc[:, 5].values
# print(elev)
# print(elev1)

map_f = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles= "Stamen Terrain")

# Adding the volcano details to the map with an info pop up about elevation
fgv = folium.FeatureGroup(name='Volcanoes')
elev_info = """ <h5>Volcano information:</h5>
                Height: %s m """
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt, ln], popup= elev_info % str(el), icon=folium.Icon(color= colour_producer(el))))

# Adding the geoJSON details: population in th JSON file
fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson( data=open('world.json', 'r', encoding='utf-8-sig').read(),
                              style_function=lambda x: {'fillColor': 'blue' if x['properties']['POP2005'] < 10000000
                                                               else 'green' if 10000000 <= x['properties']['POP2005'] <30000000
                                                               else 'orange'}))

map_f.add_child(fgv)
map_f.add_child(fgp)
map_f.add_child(folium.LayerControl())
map_f.save('check_map.html')