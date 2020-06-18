# Map
In this program I made a three layered map of the world, with volcanoes, and world population.

For the first layer, I used the folium library to create a basic interactive map of the world.

For the second layer, I used the pandas library to create a dataframe to read the contents of a csv file and 
get the name, elevation, long and lat of volcanoes in America. I then created icons to represent each volcano 
on the map based on its long and lat coordinates. Each icon had a specific color based on its elevation.

For the third layer, I extracted the world population from a JSON file and gave each area of the world a specific
color based on population size(green-low, yellow, orange, red-high).

Finally, I used a LayerControl button to toggle between layers on the website.

The program is saved as a .html file, and the map is available from there.

Attached are the csv, JSON, and html files.