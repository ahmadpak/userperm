from __future__ import unicode_literals
import frappe
from frappe import _

def get_data():
    return[
        {
            "lable": ("Setup"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Date Access Control",
                    "onboard": 1,
                }
            ]

        }
    ]