// Copyright (c) 2024, Applied Relevance and contributors
// For license information, please see license.txt

frappe.ui.form.on('Key Performance Indicator', {
    refresh: function (frm) {
        frm.set_query('base_doctype', function () {
            return {
                query: 'epistart.api.get_doctypes_with_numeric_fields'
            };
        });
    }
});

