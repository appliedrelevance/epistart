// Copyright (c) 2024, Applied Relevance and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product Requirements', {
    refresh: function (frm) {
        frm.add_custom_button(__('Sync Activities with Tasks'), function () {
            frm.call('sync_activities_with_tasks')
                .then((r) => {
                    if (r.message) {
                        frm.reload_doc();
                    }
                });
        }, __('Actions'));

        frm.add_custom_button(__('Sync Tasks with Activities'), function () {
            frm.call('sync_tasks_with_activities')
                .then((r) => {
                    if (r.message) {
                        frm.reload_doc();
                    }
                });
        }, __('Actions'));

        frm.add_custom_button(__('Sync Product Features with Tasks'), function () {
            frm.call('sync_product_features_with_tasks')
                .then((r) => {
                    if (r.message) {
                        frm.reload_doc();
                    }
                });
        }, __('Actions'));
    }
});

// Handle the real-time event for showing toast notifications
frappe.realtime.on("show_alert", function (data) {
    frappe.show_alert({
        message: data.message,
        indicator: data.indicator
    }, 5);  // Show for 5 seconds
});
