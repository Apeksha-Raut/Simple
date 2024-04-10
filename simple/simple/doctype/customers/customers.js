// Copyright (c) 2024, apeksha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customer", {
  refresh: function (frm) {
    if (!frm.is_new()) {
      // Add a custom button
      frm.add_custom_button(__("Send"), function () {
        // Get the document name
        var doc_name = frm.doc.name;

        // Make an HTTP request to another application
        frappe.call({
          method: "send_cust_id",
          args: {
            doc_name: doc_name,
          },
          callback: function (response) {
            // Handle the response
            frappe.msgprint(response.message);
          },
        });
      });
    }
  },
});
