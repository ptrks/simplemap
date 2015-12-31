
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

		self.title = title
		self.html_template = html_template
		self.center = center
		self.config = config_file
		self.markers = markers
		self._env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), trim_blocks=True, undefined=SilentUndefined)
		self._template = self._env.get_template('basic.html')


	def set_config(self, config_file):

		try:
			with open(config_file, "r") as config:    
				self._config = json.load(config)

		except IOError, e:
			print "Error, unable to open {0} config file.".format(self.config_file)
			sys.exit()

		except KeyError, e:
			print "Error, `api_entry` not found in {0} config file.".format(self.config_file)
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









	# def add_markers(self, markers):

	# 	for i in markers:

	# 		if len(i) == 2:
	# 			i.insert(0,'')
	# 	self._markers = markers


		




	def write(self, output_path):

		html = self._template.render(map_title = self.title, center=self.center, markers=self._markers, api_key=self.config['api_key'])
		with open(output_path, "w") as output:
			output.write(html)





