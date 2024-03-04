# import frappe
# # Set admission_confirm in linked Enquiry to "Admission Confirm" when Student Applicant status is "Applied"
# def on_update_student_applicant(doc, method):       
#     if doc.docstatus == 1 and doc.custom_student_enquiry:
#         frappe.db.set_value("Enquiry", doc.custom_student_enquiry, "admission_confirm", "Admission Enrolled")
