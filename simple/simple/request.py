# import requests

# def call_submit_data_api(first_name, last_name):
#     url = "http://192.168.1.252/api/method/simple.simple.api.submit_data"  # Replace "your-api-url" with the actual URL of your API endpoint
#     data = {
#         "first_name": first_name,
#         "last_name": last_name
#     }
#     response = requests.post(url, json=data)
    
#     if response.status_code == 200:
#         print("Data submitted successfully!")
#     else:
#         print("Failed to submit data. Status code:", response.status_code)
#         print("Response content:", response.text)

# # Call the function with sample data
# call_submit_data_api("apeksha","raut")

import requests

def call_submit_data_api(first_name, last_name):
    url = "http://192.168.1.252/api/method/simple.simple.api.submit_data"  # Replace with the actual URL of your API endpoint
    
    # Construct XML data
    xml_data = f"<data><first_name>{first_name}</first_name><last_name>{last_name}</last_name></data>"
    
    # Set headers to specify XML content
    headers = {'Content-Type': 'application/xml'}
    
    # Send POST request with XML data and headers
    response = requests.post(url, data=xml_data, headers=headers)
    
    if response.status_code == 200:
        print("Data submitted successfully!")
        print("Response content:")
        print(response.text)  # Print the response content
    else:
        print("Failed to submit data. Status code:", response.status_code)
        print("Response content:", response.text)

# Call the function with sample data
call_submit_data_api("John", "Doe")



# import requests

# def call_submit_data_api(xml_data):
#     url = "http://192.168.1.252/api/method/simple.simple.api.submit_data"  # Replace "your-api-url" with the actual URL of your API endpoint
    
#     # Send request with XML data
#     response = requests.post(url, data=xml_data)
    
#     if response.status_code == 200:
#         print("Data submitted successfully!")
#     else:
#         print("Failed to submit data. Status code:", response.status_code)
#         print("Response content:", response.text)

# # Construct XML data
# xml_data = "<data><first_name>Arshad</first_name><last_name>Qureshi</last_name></data>"

# # Call the function with XML data
# call_submit_data_api(xml_data)

# import requests

# # Construct XML data
# xml_data = """
# <data>
#     <first_name>Apeksha</first_name>
#     <last_name>Raut</last_name>
# </data>
# """

# # API endpoint URL
# url = "http://192.168.1.252/api/method/simple.simple.api.submit_data"  # Replace "your-api-url" with the actual URL of your API endpoint

# Send request with XML data
# response = requests.post(url, data={"xml_data": xml_data})

# if response.status_code == 200:
#     # Extract data from response
#     data = response.json()
#     print("Response:", data["message"])  # Print the message directly
# else:
#     print("Failed to submit data. Status code:", response.status_code)
#     print("Response content:", response.text)





