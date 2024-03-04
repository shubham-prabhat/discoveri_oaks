from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import cint
from frappe.permissions import has_permission

# Assuming this is a custom script for User doctype

# def custom_user_permission_query_conditions(user):
#     # If the user has the role "System Manager" or is "Administrator," allow unrestricted access
#     if "System Manager" in frappe.get_roles() or frappe.session.user == "Administrator":
#         return ""

#     # Otherwise, return a condition to restrict the list based on email matching
#     return "(`tabUser`.email = '{user}')".format(user=frappe.db.escape(user))





# # Assuming this is a custom script for User doctype

def custom_user_permission_query_conditions(user):
    # If the user is "Administrator" or has the role "System Manager," allow unrestricted access
    if frappe.session.user == "Administrator" or "System Manager" in frappe.get_roles():
        return ""

    # Otherwise, return a condition to restrict the list based on email matching
    return "(`tabUser`.email = '{user}')".format(user=frappe.session.user)







# # Assuming this is a custom script for Student doctype

def custom_student_permission_query_conditions(user):
    # If the user is "Administrator" or has the role "System Manager," allow unrestricted access
    if frappe.session.user == "Administrator" or "System Manager" in frappe.get_roles():
        return ""

    # Otherwise, return a condition to restrict the list based on user matching
    return "(`tabStudent`.student_email_id = '{user}')".format(user=frappe.session.user)




# # Assuming this is a custom script for Employee doctype


def custom_employee_permission_query_conditions(user):
    # If the user is "Administrator" or has the role "System Manager," allow unrestricted access
    if frappe.session.user == "Administrator" or "System Manager" in frappe.get_roles():
        return ""

    # Otherwise, return a condition to restrict the list based on user matching the "user_id" field
    return "(`tabEmployee`.user_id = '{user}')".format(user=frappe.session.user)




# # Assuming this is a custom script for Fee doctype

def custom_fee_permission_query_conditions(user):
    # If the user is "Administrator" or has the role "System Manager," allow unrestricted access
    if frappe.session.user == "Administrator" or "System Manager" in frappe.get_roles():
        return ""

    # Otherwise, return a condition to restrict the list based on user matching the "contact_email" field
    return "(`tabFee`.contact_email = '{user}')".format(user=frappe.session.user)
