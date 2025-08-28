import requests

# The API endpoint (URL) we want to send a GET request to
api_url = "https://api.github.com/users/google"

# Make the GET request and store the response object
response = requests.get(api_url)

# A status code is a number that tells you if the request was successful or not.
# 200 means success.
# 404 means 'Not Found'.
print(f"The status code is: {response.status_code}")

# You can also check if the request was successful using response.ok
if response.ok:
    print("Request was successful!")
else:
    print("Request failed!")