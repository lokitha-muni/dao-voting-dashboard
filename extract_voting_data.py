import requests
import json

# Use a known DAO address to test
dao_address = "0x1"  # Known active address on Aptos
url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{dao_address}/resources"

# Make the API request
response = requests.get(url)

# Check for valid status code
print("Status Code:", response.status_code)
print("Raw Response:", response.text[:500])  # Print the first 500 characters for debugging

try:
    # Parse the response as JSON
    data = response.json()

    # Print all the available module types
    print("\nParsed JSON Types:\n")
    for item in data:
        print(item['type'])

    # Look for VotingForum related data and pretty print it
    for item in data:
        if item['type'].startswith("0x1::voting::VotingForum"):
            print("\nFound VotingForum Data:")
            print(json.dumps(item, indent=2))  # Pretty print the VotingForum data

except json.JSONDecodeError:
    print("⚠️ Error: Couldn't decode JSON response")
except Exception as e:
    print("⚠️ Some other error:", e)
