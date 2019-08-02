# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "userperm"
app_title = "User Activity Management"
app_publisher = "Havenir"
app_description = "To control the access level of users"
app_icon = "octicon octicon-organization"
app_color = "green"
app_email = "info@havenir.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/userperm/css/userperm.css"
# app_include_js = "/assets/userperm/js/userperm.js"

# include js, css files in header of web template
# web_include_css = "/assets/userperm/css/userperm.css"
# web_include_js = "/assets/userperm/js/userperm.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

doctype_js = {
    "Sales Order"   :   [
        "utils/sales_invoice.js"
    ],
    "Delivery Note"   :   [
        "utils/sales_invoice.js"
    ],
    "Sales Invoice" :   [
        "utils/sales_invoice.js"
    ],
    "Purchase Order"   :   [
        "utils/sales_invoice.js"
    ],
    "Purchase Receipt"   :   [
        "utils/sales_invoice.js"
    ],
    "Purchase Invoice" :[
        "utils/purchase_invoice.js"
    ]
}


#doctype_list_js = {
#    "Sales Invoice" : [
#        "utils/sales_invoice_list.js"
#    ]
#}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "userperm.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "userperm.install.before_install"
# after_install = "userperm.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "userperm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"userperm.tasks.all"
# 	],
# 	"daily": [
# 		"userperm.tasks.daily"
# 	],
# 	"hourly": [
# 		"userperm.tasks.hourly"
# 	],
# 	"weekly": [
# 		"userperm.tasks.weekly"
# 	]
# 	"monthly": [
# 		"userperm.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "userperm.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "userperm.event.get_events"
# }

