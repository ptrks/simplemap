import simplemap

map_title = 'Example Map'
center_point  = [34.5124, -118.1111]
#center_point = None

gps_markers = [ ['Example text', 34.4563,-118.1241], [34.5235,-118.1245], [34.6432,-118.1554] ]
# TIL that python asigns by reference. Meaning that even though you shift data around in new_gps
# it will effect the original :|. To avoid this I could have done `new_gps = gps_makers[:]` which 
# would have made a new list. The issue is gps_markers is a 2 dimensional array/list, so it was only
# looking one level deep. So we need to go deeper morty.
new_gps = [sublist[:] for sublist in gps_markers]

# This is how I have it the following in my provate repo. Couldn't work out how to add it to map.py
# It is also completley optioinal. Simply remove the 'points' argument in the example_map below.
# Here we change the formatting of the waypoints so gmaps api can use them to plot lines
def make_points(coords):
	if(coords):
		# Firstly we don't want the hover text.
		for x in range(0, len(coords)):
			if(len(coords[x]) == 3):
				coords[x].pop(0)
		# List comprehensions are fun. Basically telling it the format I want and then it has its 
		# own little for loop and then changes all elements. It's more obvious when you look at
		# var points in a generated html file.
		new_list = [{'lat': d[0], 'lng': d[1]} for d in coords]
		# Return the new list after the list comprehension.
	return new_list

new_gps = make_points(new_gps)


example_map = simplemap.Map(map_title, markers=gps_markers, points=new_gps)
example_map.write('example.html')