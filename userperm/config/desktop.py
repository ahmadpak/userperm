# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "User Activity Management",
			"category": "Modules",
			"label": _("User Activity Management"),
			"color": "green",
			"icon": "octicon octicon-organization",
			"type": "module",
			"onboard_present": 1
		}
	]
