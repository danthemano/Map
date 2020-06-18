import folium
import pandas

#create a Map object, passing: a location coordinates, tiles which represent the design of the map, zoom which is the broad overview
map = folium.Map(location=[40.7608, -111.8910], tiles= "Stamen Terrain", zoom_start=6)

#creates a dataframe and loads it with the volcano information
data = pandas.read_csv("Volcanoes.txt")

#creates lists that contain the longitude, latitude, the elevation, and the name of the volcanoes
latitude = list(data["LAT"])
longitude = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])

#this functions takes an elevation and returns the matching color
def color(elevation):
    if(elevation < 1500):
        return 'green'
    elif(1500 < elevation < 3000):
        return 'orange'
    else:
        return 'red'


#creates a feature group for the volcano layer
feature_group_V = folium.FeatureGroup(name="Volcanoes")

#loops through the volcanoes and adds them as icons to the map with colors matching their elevation
for lat, lon, v_name, elev in zip(latitude, longitude, name, elevation):
    feature_group_V.add_child(folium.Marker(location=[lat, lon], popup=v_name, icon=folium.Icon(color=color(elev))))

#creates a feature group for the world population layer
feature_group_P = folium.FeatureGroup(name="Population")

#Reads population from a JSON file and groups them by colors based on their size.
feature_group_P.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
        style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                       else 'yellow' if 10000000 <= x['properties']['POP2005'] <= 20000000
                                                       else 'orange' if 10000000 <= x['properties']['POP2005'] <= 50000000
                                                       else 'red'}))

#adds the feature group onto the map
map.add_child(feature_group_V)
map.add_child(feature_group_P)

#LayerControl allows us to switch between different layers
map.add_child(folium.LayerControl())

#translate the object into html
map.save("Map1.html")
