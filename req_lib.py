import requests

# Proposal handle
proposal_handle = "0x38ff67f17cf7998cd41ed5267b52cff7af37d06a22e8b390ce44b69680fc0e97"

# API URL to fetch the proposal data
url = f"https://api.aptos.dev/v1/proposals/{proposal_handle}"

# Send the GET request to the API
response = requests.get(url)

# Check the status code
if response.status_code == 200:
    # Parse the response JSON data
    proposal_data = response.json()
    print(proposal_data)
else:
    print(f"Failed to fetch proposal data: {response.status_code}")
