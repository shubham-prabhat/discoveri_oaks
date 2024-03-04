# import frappe
# @frappe.whitelist()
# def validate_student_enquiry_association(doc, method):
#     # Get the value of the custom_student_enquiry field
#     custom_student_enquiry = doc.get('custom_student_enquiry')

#     # Check if the value is not empty
#     if custom_student_enquiry:
#         # Get all custom_student_enquiry values from "Student Applicant" doctype
#         student_applicant_values = get_student_applicant_values(custom_student_enquiry, doc.name)

#         # Check if the current custom_student_enquiry value matches any value in "Student Applicant"
#         if student_applicant_values:
#             frappe.throw('The "Student Enquiry" field value is already associated with another "Student Applicant" form.')

# def get_student_applicant_values(custom_student_enquiry, docname):
#     # Query to check if the current custom_student_enquiry value matches any value in "Student Applicant"
#     query = """
#         SELECT name
#         FROM `tabStudent Applicant`
#         WHERE custom_student_enquiry = %s
#         AND name != %s
#     """

#     result = frappe.db.sql(query, (custom_student_enquiry, docname))

#     return result














import frappe

@frappe.whitelist()
def validate_student_enquiry_association(doc, method):
    # Get the value of the custom_student_enquiry field
    custom_student_enquiry = doc.get('custom_student_enquiry')

    # Check if the value is not empty
    if custom_student_enquiry:
        # Get all custom_student_enquiry values from "Student Applicant" doctype
        student_applicant_names = get_student_applicant_names(custom_student_enquiry, doc.name)

        # Check if the current custom_student_enquiry value matches any value in "Student Applicant"
        if student_applicant_names:
            names_str = ', '.join(student_applicant_names)
            frappe.throw(f'The "Student Enquiry" field value is already associated with another "Student Applicant" form. Document Names: {names_str}')

def get_student_applicant_names(custom_student_enquiry, docname):
    # Query to check if the current custom_student_enquiry value matches any value in "Student Applicant"
    query = """
        SELECT name
        FROM `tabStudent Applicant`
        WHERE custom_student_enquiry = %s
        AND name != %s
    """

    result = frappe.db.sql(query, (custom_student_enquiry, docname))

    # Extract document names from the result
    return [record[0] for record in result]















# # # # Updating field value 'admission_status' tbased on "Student Applicant" form admission status


# Set admission_confirm in linked Enquiry to "Admission Confirm" when Student Applicant status is "Applied"
def on_update_student_applicant(doc, method):
    if doc.application_status == "Applied" and doc.custom_student_enquiry:
        frappe.db.set_value("Enquiry", doc.custom_student_enquiry, "admission_status", "Admission Applied")
        
    if doc.application_status == "Approved" and doc.custom_student_enquiry:
        frappe.db.set_value("Enquiry", doc.custom_student_enquiry, "admission_status", "Admission Confirmed")
        
    if doc.application_status == "Rejected" and doc.custom_student_enquiry:
        frappe.db.set_value("Enquiry", doc.custom_student_enquiry, "admission_status", "Cancelled")
 