import requests
import json

def fetch_voting_data():
    try:
        # Replace with the correct URL for fetching voting data from Aptos API
        url = "https://api.aptos.org/v1/governance/proposals"
        response = requests.get(url)
        response.raise_for_status()  # Raises exception for HTTP errors
        data = response.json()  # Assuming the response is in JSON format
        
        # Print the raw JSON response for debugging
        print("Fetched data:", json.dumps(data, indent=4))

        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
