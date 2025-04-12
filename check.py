import requests
import json

url = "https://api.mainnet.aptoslabs.com/v1"
response = requests.get(url)
print(response.status_code)
print(response.text)

# Check if the response status is OK (status code 200)
if response.status_code == 200:
    try:
        data = response.json()  # Try to parse the JSON data
        if data:
            print("Data fetched successfully:")
            print(json.dumps(data, indent=4))  # Pretty print the JSON data
        else:
            print("No data found in the response.")
    except json.JSONDecodeError:
        print("Error decoding JSON: The response body is not valid JSON.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print("Response content:", response.text)
