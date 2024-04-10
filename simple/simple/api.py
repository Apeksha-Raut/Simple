import frappe
from frappe import _

# @frappe.whitelist(allow_guest=True)
# def receive_data():
#     data = frappe.request.data

#     # Process the data if needed
    
#     # Return a response, e.g., in JSON format
#     #return {"message: Hello"}
#     #retuen a response  data from database
#     return frappe.db.sql(f"""select first_name from `tabEmployee` where department="Information Technology";""")

# @frappe.whitelist(allow_guest=True)
# def receive_data():
#     # Fetch data from the database or get it from somewhere else
#     first_name = "John"
#     last_name = "Doe"
#     age = "30"
    
#     # Construct XML document
#     xml_data = f"<employee><first_name>{first_name}</first_name><last_name>{last_name}</last_name><age>{age}</age></employee>"

#     return xml_data

# import frappe
# from frappe import _

# @frappe.whitelist(allow_guest=True)
# def get_employees():
#     xml_data = """<employees>
#                     <employee>
#                         <first_name>John</first_name>
#                         <last_name>Doe</last_name>
#                         <age>30</age>
#                     </employee>
#                     <employee>
#                         <first_name>Jane</first_name>
#                         <last_name>Smith</last_name>
#                         <age>25</age>
#                     </employee>
#                 </employees>"""
    
#     # Set the Content-Type header to specify XML response
#     frappe.response['content_type'] = 'application/xml'
#     return xml_data



# @frappe.whitelist(allow_guest=True)
# def submit_data(first_name, last_name):
#     doc = frappe.new_doc("API Demo")
#     doc.first_name = first_name
#     doc.last_name = last_name
#     doc.insert(ignore_permissions=True)
#     return _("Data submitted successfully!")

import frappe
from xml.etree import ElementTree as ET

@frappe.whitelist(allow_guest=True)
def submit_data():
    # Parse XML data from the request
    xml_data = frappe.request.data
    root = ET.fromstring(xml_data)

    # Extract first_name and last_name from XML
    first_name = root.find('first_name').text
    last_name = root.find('last_name').text

    # Create a new document and insert data
    doc = frappe.new_doc("API Demo")
    doc.first_name = first_name
    doc.last_name = last_name
    doc.insert(ignore_permissions=True)

    return _("Data submitted successfully!")


# import frappe
# from xml.etree import ElementTree as ET

# @frappe.whitelist(allow_guest=True)
# def submit_data(xml_data):
#     try:
#         # Parse XML data
#         root = ET.fromstring(xml_data)
        
#         # Extract first_name and last_name from XML
#         first_name = root.find('first_name').text
#         last_name = root.find('last_name').text

#         # Create a new document
#         doc = frappe.new_doc("API Demo")
#         doc.first_name = first_name
#         doc.last_name = last_name
#         doc.insert(ignore_permissions=True)

#         return _("Data submitted successfully!")
#     except Exception as e:
#         frappe.log_error(f"Error submitting data: {e}")
#         return _("Failed to submit data. Please check the XML format and log for errors.")


# import frappe
# from xml.etree import ElementTree as ET
# from urllib.parse import unquote
# import json

# @frappe.whitelist(allow_guest=True)
# def submit_data(xml_data):
#     try:
#         if not xml_data:
#             return {"error": "No XML data provided."}

#         # Decode XML data (if URL encoded)
#         xml_data = unquote(xml_data)

#         # Print XML data for debugging
#         print("XML Data:", xml_data)
    
    
#         # Parse XML data
#         root = ET.fromstring(xml_data)
        
#         # Extract first_name and last_name from XML
#         first_name = root.find('first_name').text
#         last_name = root.find('last_name').text

#         # Format the data
#         data = {"first_name": first_name, "last_name": last_name}

#         # Return the data
#         return data

#         # # Create a new document in the API Demo doctype
#         # doc = frappe.new_doc("API Demo")
#         # doc.first_name = first_name
#         # doc.last_name = last_name
#         # doc.insert()

#         # Return success message
#         return {"message": "Document created successfully."}
#     except Exception as e:
#         frappe.log_error(f"Error creating document: {e}")
#         return {"error": "Failed to create document. Please check the XML format."}  

# import frappe
# # import json
# # import xmltodict
# from urllib.parse import unquote
# from xml.etree import ElementTree as ET


# @frappe.whitelist(allow_guest=True)
# def submit_data(xml_data):
#     try:
#         # Parse XML data
#         root = ET.fromstring(xml_data)
        
#         # Extract first_name and last_name from XML
#         first_name = root.find('first_name').text
#         last_name = root.find('last_name').text

#         # Format the data
#         data = {"first_name": first_name, "last_name": last_name}
        
#         # Return the data
#         return {"status": "success", "data": data}
#     except Exception as e:
#         # Handle errors gracefully
#         return {"status": "error", "message": str(e)}


# import requests
# import xml.etree.ElementTree as ET
# import frappe

#@frappe.whitelist(allow_guest=True)
#def submit_data(xml_data):
    # try:
        
        # # Check if the request was successful (status code 200)
        # if xml_data.status_code == 200:
        #     # Parse the XML response
        #     root = ET.fromstring(xml_data)
            
        #     # Extract data from XML
        #     first_name = root.find('firstName').text
        #     last_name = root.find('lastName').text
            
            # # Create a new ShareTest document with first_name and last_name
            # doc = frappe.new_doc('API Demo')
            # doc.first_name = first_name
            # doc.last_name = last_name
            
            # # Insert the document into the database
            # doc.insert()
            
   # return xml_data
    #     else:
    #         frappe.log_error(f"Failed to fetch data from API. Status code: {xml_data.status_code}")
    #         return False
    # except Exception as e:
    #     # Handle any exceptions that occur during the request
    #     frappe.log_error(f"Error receiving data from API: {e}")
    #     return False



# @frappe.whitelist(allow_guest=True)
# def submit_data(xml_data):
#     try:
#         if not xml_data:
#             return {"error": "No XML data provided."}

#         # Decode XML data (if URL encoded)
#         xml_data = unquote(xml_data)

#         # Print XML data for debugging
#         print("XML Data:", xml_data)

#         # Convert XML data to dictionary using xmltodict
#         data = xmltodict.parse(xml_data)

#         # Print dictionary data for debugging
#         print("Dictionary Data:", data)

#         # Convert dictionary to JSON
#         json_data = json.dumps(data)

#         # Print JSON data for debugging
#         print("JSON Data:", json_data)

#         # Create a new document in the "API Demo" doctype
#         doc = frappe.new_doc("API Demo")

#         # Set fields from the converted dictionary
#         for key, value in data.items():
#             doc.set(key, value)

#         doc.insert()

#         # Return success message
#         return {"message": "Document created successfully."}

#     except Exception as e:
#         frappe.log_error(f"Error creating document: {e}")
#         return {"error": "Failed to create document. Please check the XML format."}




@frappe.whitelist(allow_guest=True)
def ping():
    return "pong"



# import requests

# url = 'http://192.168.1.252/api/method/simple.simple.api.submit_data'
# data = {
#     'first_name': 'arshad',
#     'last_name': 'qureshi'
# }
# response = requests.post(url, json=data)
# print(response.text)



# @frappe.whitelist(allow_guest=True)
# def submit_data(xml_data):
#     try:
#         # Parse the XML data to extract necessary information
#         # For example, if the XML structure is known:
#         print(xml_data)

#         import xml.etree.ElementTree as ET
#         root = ET.fromstring(xml_data)
#         first_name = root.find('first_name').text
#         last_name = root.find('last_name').text

#         # Create a new document in the "API Demo" doctype
#         doc = frappe.get_doc({
#             "doctype": "API Demo",
#             "first_name": first_name,
#             "last_name": last_name
#             # Add other fields as necessary
#         })
#         doc.insert(ignore_permissions=True)

#         return _("Document created successfully"), 200
#     except Exception as e:
#         frappe.throw(_("Error creating document: {0}".format(e)))

# import frappe
# from frappe import _

# @frappe.whitelist(allow_guest=True)
# def submit_data(xml_data):
#     try:
#         # Print the XML data to inspect its contents
#         return xml_data

#         # Continue with XML parsing and document creation logic
#         # ...
#     except Exception as e:
#         frappe.throw(_("Error: {0}".format(e)))
