# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "User Activity Management",
			"color": "green",
			"icon": "octicon octicon-organization",
			"type": "module",
			"label": _("User Activity Management"),
			"items":[
				{
					"type": "doctype",
					"name": "Date Access Control",
					"lable": _("Date Access Control"),
					"description": _("Invoke user access for not included period")
				}
			]
		}
	]
