# import frappe
# from frappe import _

# @frappe.whitelist(allow_guest=True)
# def create(share_ac_no, cust_name):
#     try:
#         doc = frappe.new_doc("Customers")
#         doc.customer_name = cust_name
#         doc.share_ac_no = share_ac_no
#         doc.insert(ignore_permissions=True)
#         frappe.db.commit()  # Commit the transaction to ensure the document is saved in the database
#         return {"message": _("Data submitted successfully!"), "docname": doc.name}
#     except frappe.DuplicateEntryError:
#         return {"message": _("Share account number already exists! Please provide a unique share account number."), "docname": ""}

import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create(share_ac_no, cust_name):
    # Check if the share_ac_no already exists
    existing_doc = frappe.db.exists("Customers", {"share_ac_no": share_ac_no})
    if existing_doc:
        return {"message": _("Share account number already exists! Please provide a unique share account number."), "docname": ""}
    
    # Create the document if share_ac_no is unique
    try:
        doc = frappe.new_doc("Customers")
        doc.customer_name = cust_name
        doc.share_ac_no = share_ac_no
        doc.insert(ignore_permissions=True)
        frappe.db.commit()  # Commit the transaction to ensure the document is saved in the database
        return {"message": _("Data submitted successfully!"), "docname": doc.name}
    except frappe.exceptions.UniqueValidationError:
        return {"message": _("Share account number already exists! Please provide a unique share account number."), "docname": ""}
