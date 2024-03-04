app_name = "discoveri_oaks"
app_title = "Discoveri Oaks"
app_publisher = "Blue Cloud"
app_description = "Discoveri Oaks Learning Forward"
app_email = "shubham.prabhat@bluecloud.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/discoveri_oaks/css/discoveri_oaks.css"
# app_include_js = "/assets/discoveri_oaks/js/discoveri_oaks.js"

# include js, css files in header of web template
# web_include_css = "/assets/discoveri_oaks/css/discoveri_oaks.css"
# web_include_js = "/assets/discoveri_oaks/js/discoveri_oaks.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "discoveri_oaks/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "discoveri_oaks/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "discoveri_oaks.utils.jinja_methods",
# 	"filters": "discoveri_oaks.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "discoveri_oaks.install.before_install"
# after_install = "discoveri_oaks.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "discoveri_oaks.uninstall.before_uninstall"
# after_uninstall = "discoveri_oaks.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "discoveri_oaks.utils.before_app_install"
# after_app_install = "discoveri_oaks.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "discoveri_oaks.utils.before_app_uninstall"
# after_app_uninstall = "discoveri_oaks.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "discoveri_oaks.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"discoveri_oaks.tasks.all"
# 	],
# 	"daily": [
# 		"discoveri_oaks.tasks.daily"
# 	],
# 	"hourly": [
# 		"discoveri_oaks.tasks.hourly"
# 	],
# 	"weekly": [
# 		"discoveri_oaks.tasks.weekly"
# 	],
# 	"monthly": [
# 		"discoveri_oaks.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "discoveri_oaks.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "discoveri_oaks.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "discoveri_oaks.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["discoveri_oaks.utils.before_request"]
# after_request = ["discoveri_oaks.utils.after_request"]

# Job Events
# ----------
# before_job = ["discoveri_oaks.utils.before_job"]
# after_job = ["discoveri_oaks.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"discoveri_oaks.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }



doc_events = {
    "Enquiry": {
        "on_update": [
            "discoveri_oaks.discoveri_oaks.doctype.enquiry.enquiry.send_email_on_status_change",
            "discoveri_oaks.discoveri_oaks.doctype.enquiry.enquiry.send_emails",
        ],
        "on_cancel": [
            # "blue_cloud.blue_cloud.doctype.book_issue.book_issue.on_cancel",
        ]
    },
    "Student Applicant": {
        "on_update": [
            "discoveri_oaks.discoveri_oaks.doctype.student_applicant.student_applicant.validate_student_enquiry_association",
            "discoveri_oaks.discoveri_oaks.doctype.student_applicant.student_applicant.on_update_student_applicant"
        ],
        "on_cancel": [
            # "blue_cloud.blue_cloud.doctype.book_issue.book_issue.on_cancel",
        ]
    }
}






app_include_js = [
    # "/assets/discoveri_oaks/js/enquiry.js",
    "/assets/discoveri_oaks/js/student_applicant.js"
]



# hooks.py or custom_hooks.py

permission_query_conditions = {
    "User": "discoveri_oaks.permission_condition.custom_user_permission_query_conditions",
    "Student": "discoveri_oaks.permission_condition.custom_student_permission_query_conditions",
    "Employee": "discoveri_oaks.permission_condition.custom_employee_permission_query_conditions"
}
