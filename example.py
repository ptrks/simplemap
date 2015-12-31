import simplemap

map_title = 'Example Map'
center_point  = [34.5124, -118.1111]
gps_markers = [ ['Example text', 34.4563,-118.1241], [34.6432,-118.1554] ]

example_map = simplemap.Map(map_title, center_point, markers=gps_markers, config_file='dev_config.json')
example_map.write('example.html')