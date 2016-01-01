
"""
simplemap.map.py
~~~~~~~~~~~~~~~~

This module contains all core functionality related to map generation

"""

from jinja2 import Environment, FileSystemLoader
from html_render import SilentUndefined
import json
import os
import sys
import traceback

TEMPLATES_DIR = FileSystemLoader('simplemap/templates')
ZOOM_DEFAULT = 11

class Map(object):
	def __init__(self, title, center=None, zoom=11, markers=None, html_template='basic.html', config_file='config.json'):
		self._env = Environment(loader=TEMPLATES_DIR, trim_blocks=True, undefined=SilentUndefined)
		self.title = title
		self.template = self._env.get_template(html_template)
		self.center = center
		self.zoom = zoom
		self.config = config_file
		self.markers = markers

	def set_center(self, center_point):
		self._center = '{{ lat:{}, lng:{}}}'.format(*center_point) if center_point else 'null'

	def get_center(self):
		return self._center

	def set_zoom(self, zoom):
		if zoom:
			self._zoom = zoom
		else:
			#Don't allow zoom to be null if customer center is given 
			self._zoom = ZOOM_DEFAULT if self.center else 'null'

	def get_zoom(self):
		return self._zoom
	
	def set_config(self, config_file):
		try:
			with open(config_file, "r") as config:    
				self._config = json.load(config)
		except IOError:
			sys.exit("Error, unable to open {} config file.".format(config_file))
		except KeyError:
			sys.exit("Error, `api_entry` not found in {} config file.".format(config_file))
		except Exception:
			print "An unknown error occured while attempting to read {} config file.".format(config_file)
			traceback.print_exc()
			sys.exit()

	def get_config(self):
		return self._config

	def set_markers(self, markers):
		if markers:
			for i in markers:
				if len(i) == 2:
					i.insert(0, '')
			self._markers = markers

	def get_markers(self):
		return self._markers

	config = property(get_config, set_config)
	markers = property(get_markers, set_markers)
	center = property(get_center, set_center)
	zoom = property(get_zoom, set_zoom)

	def write(self, output_path):
		try:
			html = self.template.render(map_title = self.title, center=self.center,
				zoom=self.zoom, markers=self.markers, api_key=self.config['api_key'])
			with open(output_path, "w") as out_file:
				out_file.write(html)
			return 'file://' + os.path.join(os.path.abspath(os.curdir), output_path)
		except IOError:
			sys.exit("Error, unable to write {}".format(output_path))
		except Exception:
			print "Undefined error occured while writing generating {}".format(output_path)
			traceback.print_exc()
			sys.exit()
