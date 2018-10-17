import simplemap, webbrowser

map_title = 'Example Map'
center_point  = [34.5124, -118.1111]
#center_point = None

gps_markers = [ ['Example text', 34.4563,-118.1241], [34.5235,-118.1245], [34.6432,-118.1554] ]
# TIL that python asigns by reference. Meaning that even though you shift data around in new_gps
# it will effect the original :|. To avoid this I could have done `new_gps = gps_makers[:]` which 
# would have made a new list. The issue is gps_markers is a 2 dimensional array/list, so it was only
# looking one level deep. So we need to go deeper morty.
new_gps = [sublist[:] for sublist in gps_markers]

example_map = simplemap.Map(map_title, markers=gps_markers)
file_url = example_map.write('example.html')
print('HTML page written to: ' + file_url)
webbrowser.open(file_url)