// Define the data to be sent in the request body
const data = {
  first_name: "apeksha",
  last_name: "raut",
};

// Define the URL of the API endpoint
const url = "http://192.168.1.252/api/method/simple.simple.api.submit_data";

// Define options for the fetch request
const options = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(data),
};

// Make the fetch request
fetch(url, options)
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json(); // Parse response body as JSON
  })
  .then((data) => {
    // Handle successful response
    console.log("Response:", data);
  })
  .catch((error) => {
    // Handle error
    console.error("There was a problem with the fetch operation:", error);
  });
