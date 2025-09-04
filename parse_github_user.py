import requests
import json

# The API endpoint (URL) we want to send a GET request to
api_url = "https://api.github.com/users/google"

# Make the GET request and store the response object
response = requests.get(api_url)

# Check if the request was successful
if response.ok:
    # The response.text attribute gives us the raw JSON string
    json_string_data = response.text

    # Use json.loads() to parse the JSON string into a Python dictionary
    user_data = json.loads(json_string_data)

    # Access the user's name and location from the dictionary
    user_name = user_data.get("name")
    user_location = user_data.get("location")

    # Print the results
    print(f"User Name: {user_name}")
    print(f"Location: {user_location}")
else:
    print(f"Error: API request failed with status code {response.status_code}")