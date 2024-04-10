# Demo code sample. Not indended for production use.

# See instructions for installing Requests module for Python
# https://requests.readthedocs.io/en/master/user/install/#install

from simple.API.create_customer import create
import requests

# URL for the API endpoint
url = "http://192.168.1.252/api/method/simple.API.create_customer.create"

# Sample data
data = {
    "share_ac_no": "98009",
    "cust_name": "Talib Sheikh"
}

# Making the POST request to the API
response = requests.post(url, json=data)

# Checking the response
if response.status_code == 200:
    result = response.json()
    print(result["message"])
    # print("Created document name:", result["docname"])
else:
    print("Error:", response.text)
