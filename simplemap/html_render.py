
"""
simplemap.html_render
~~~~~~~~~~~~~~~~~~~~~

This module contains everything related to Jinja2 HTML rendering.
"""

from jinja2 import Undefined


class SilentUndefined(Undefined):
	""" Allow Jinja2 to continue rendering if undefined tag is parsed """

	def _fail_with_undefined_error(self, *args, **kwargs):
		return None