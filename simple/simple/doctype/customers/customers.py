# Copyright (c) 2024, apeksha and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from frappe import _


class Customers(Document):
	pass




@frappe.whitelist()
def send_cust_id(doc_name):
    # Perform actions to send the document name to another application
    # For example, you can use libraries like requests to make an HTTP request
    # to the other application's endpoint
    # Example:
    # response = requests.post("http://example.com/api", json={"doc_name": doc_name})
    # handle_response(response)
    
    # Dummy response for demonstration
    return _("Document name '{}' sent to another application.").format(doc_name)
