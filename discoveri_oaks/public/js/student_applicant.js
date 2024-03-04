    frappe.ui.form.on('Student Applicant', {
        refresh: function(frm) {
            // Add a filter to custom_student_enquiry based on linked Enquiry's docstatus
            frm.fields_dict['custom_student_enquiry'].get_query = function(doc, cdt, cdn) {
                var enquiry = locals[cdt][cdn].enquiry;
                return {
                    filters: {
                        docstatus: 1, // Filter by Enquiry documents with docstatus = 1
                        admission_status: ['not in', ['Cancelled']]
                    }
                };
            };
        }
    });


        frappe.ui.form.on('Student Applicant', {
            refresh: function(frm) {
                // Check if the document is submitted (docstatus = 1)
                if (frm.doc.docstatus === 1) {
                    // Add a custom button to the form
                    frm.add_custom_button(__('Know About Your Child'), function() {
                        // Redirect to the "Know About Your Child" doctype with a new document
                        frappe.route_options = {
                            student_applicant_form: frm.doc.name
                        };
                        frappe.new_doc('Know About Your Child');
                    });
                }
            }
        });
    

