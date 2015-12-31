import simplemap

 
example = simplemap.Map('Example Map', [51.503454, -0.119562], markers=[[ 51.503454, -0.119562],[51.499633, -0.124755 ]], config_file='dev_config.json')


example.write('output4.html')