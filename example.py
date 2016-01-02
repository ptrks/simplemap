import simplemap

map_title = 'Example Map'
center_point  = [34.5124, -118.1111]
#center_point = None

gps_markers = [ [34.4563, -118.1241, ['Example Text', 'Test']], [34.6432,-118.1554], [34.5124, -118.1111, ['', '']]]

example_map = simplemap.Map(map_title, markers=gps_markers)
example_map.write('example.html')
