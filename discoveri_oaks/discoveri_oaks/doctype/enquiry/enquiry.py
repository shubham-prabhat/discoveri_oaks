
from __future__ import unicode_literals
# Copyright (c) 2024, Blue Cloud and contributors
# For license information, please see license.txt

# import frappe

from frappe.model.document import Document


class Enquiry(Document):
	pass





import frappe
# from __future__ import unicode_literals
import frappe
from frappe.utils import nowdate

# def send_email_on_status_change(doc, method):
#     if doc.docstatus == 1:
#         recipient_email = doc.email
#         email_template = doc.email_template

#         if email_template:
#             template = frappe.get_doc("Email Template", email_template)
#             subject = template.subject
#             message = template.response
#         else:
#             subject = "Enquiry Status Update"
#             message = " Hi doc.first_name, Your enquiry has been processed."

#         frappe.sendmail(recipients=recipient_email, subject=subject, message=message)










def send_email_on_status_change(doc, method):
    if doc.docstatus == 1:
        recipient_email = doc.primary_email_id
        email_template = doc.email_template

        if email_template:
            template = frappe.get_doc("Email Template", email_template)
            subject = template.subject
            # Replace placeholders in the email response with actual values
            message = template.response.replace('{{ doc.full_name }}', doc.full_name)
            # message = template.response.replace('{{ doc.full_name}}', doc.first_name).replace('{{ doc.last_name }}', doc.last_name)
        else:
            subject = "Enquiry Status Update"
            # Format the message with the dynamic value of doc.first_name
            message = f"Hi {doc.full_name}, Your enquiry has been processed."

        frappe.sendmail(recipients=recipient_email, subject=subject, message=message)






def send_emails(doc, method):
    if doc.docstatus == 1:
        # Your email sending logic here
        email_queue_list = frappe.get_list('Email Queue', filters={'status':'Not Sent'}, limit=100000000)
        for email_queue in email_queue_list:
            print('Sending', email_queue.name)
            frappe.call('frappe.email.doctype.email_queue.email_queue.send_now', {
                'name': email_queue.name,
            })

# # Register the send_emails function to be called when an Enquiry document is updated
# def setup_hooks():
#     frappe.db.after_commit(lambda: send_emails(frappe.get_doc("Enquiry", frappe.local.form_dict.get("name")), "on_update"))









# def send_email_on_status_change(doc, method):
#     if doc.docstatus == 1:
#         recipient_email = doc.email
#         email_template = doc.email_template

#         if email_template:
#             template = frappe.get_doc("Email Template", email_template)
#             subject = template.subject
#             message = template.response
#         else:
#             subject = "Enquiry Status Update"
#             message = " Hi doc.first_name, Your enquiry has been processed."

#         frappe.sendmail(recipients=recipient_email, subject=subject, message=message)
#         frappe.msgprint("Email Sent")
