// Copyright (c) 2024, Applied Relevance and contributors
// For license information, please see license.txt

frappe.ui.form.on('Competitor Analysis', {
    onload: function (frm) {
        // Check if the 'Competitor' doctype exists in ERPNext
        frappe.db.exists('DocType', 'Competitor')
            .then(exists => {
                // If the doctype exists, show the link field
                if (exists) {
                    frm.set_df_property('crm_competitor', 'hidden', false);
                } else {
                    // Otherwise, hide the link field
                    frm.set_df_property('crm_competitor', 'hidden', true);
                }
            });
    }
});

