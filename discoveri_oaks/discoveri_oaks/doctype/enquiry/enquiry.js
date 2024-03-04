// Copyright (c) 2024, Blue Cloud and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Enquiry", {
// 	refresh(frm) {

// 	},
// });


// // //  // automatic calculating the age of students based on "date_of_birth" field

frappe.ui.form.on('Enquiry', {
    date_of_birth: function(frm) {
        // Calculate age based on date_of_birth
        calculateAge(frm);
    }
});

function calculateAge(frm) {
    // Get the date_of_birth value
    var dob = frm.doc.date_of_birth;

    if (dob) {
        // Check if the selected date is in the future
        if (frappe.datetime.get_diff(dob, frappe.datetime.now_date()) < 0) {
            // Calculate age in years
            var age = frappe.datetime.get_diff(frappe.datetime.now_date(), dob) / 365.25;
            age = Math.floor(age);

            // Set the calculated age in the age field
            frm.set_value('age', age);
        } else {
            frappe.msgprint(__('Date of Birth cannot be in the future.'));
            frm.set_value('date_of_birth', '');
            frm.set_value('age', '');
        }
    } else {
        // Clear both fields if date_of_birth has no value
        frm.set_value('date_of_birth', '');
        frm.set_value('age', '');
    }
}



// // // Validating the field for "Select" Field

frappe.ui.form.on('Enquiry', {
    validate: function(frm) {
        // Check if income is set to the default value "Select"
        if (frm.doc.income === 'Select') {
            frappe.msgprint(__('Please select a valid income value.'));
            frappe.validated = false; // Prevent saving the form
        }

        // Check if know_about_us is set to the default value "Select"
        if (frm.doc.know_about_us === 'Select') {
            frappe.msgprint(__('Please select a valid "Know About Us" value.'));
            frappe.validated = false; // Prevent saving the form
        }

        // Check if know_about_us is set to the default value "Select"
        if (frm.doc.board === 'Select') {
            frappe.msgprint(__('Please select a valid "Board" value.'));
            frappe.validated = false; // Prevent saving the form
        }
    }
});