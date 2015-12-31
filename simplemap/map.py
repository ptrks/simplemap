
"""
simplemap.map.py
~~~~~~~~~~~~~~~~

This module contains all core functionality related to map generation

"""

from jinja2 import Environment, FileSystemLoader
from html_render import SilentUndefined
import json
import traceback
import sys


TEMPLATES_DIR = 'simplemap/templates'

class Map(object):

	def __init__(self, title, center, zoom=11, markers=None, html_template='basic.html', config_file='config.json'):

		self._env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), trim_blocks=True, undefined=SilentUndefined)

		self.title = title
		self.template = self._env.get_template(html_template)
		self.center = center
		self.config = config_file
		self.markers = markers

	
	def set_config(self, config_file):

		try:
			with open(config_file, "r") as config:    
				self._config = json.load(config)

		except IOError:
			print "Error, unable to open {0} config file.".format(config_file)
			sys.exit()

		except KeyError:
			print "Error, `api_entry` not found in {0} config file.".format(config_file)
			sys.exit()

		except Exception:
			print "An unknown error occured while attempting to read {0} config file.".format(config_file)


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


	def write(self, output_path):

		try:

			html = self.template.render(map_title = self.title, center=self.center, markers=self._markers, api_key=self.config['api_key'])
			with open(output_path, "w") as output:
				output.write(html)

		except IOError:
			print "Error, unable to write {0}".format(output_path)
			sys.exit()

		except Exception:
			print "Undefined error occured while writing generating {0}".format(output_path)
			sys.exit(0)





