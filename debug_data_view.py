import requests
import json

# Replace this URL with your actual Aptos API endpoint
url = "https://fullnode.mainnet.aptoslabs.com/v1/accounts/0x38ff67f17cf7998cd41ed5267b52cff7af37d06a22e8b390ce44b69680fc0e97/resources"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Pretty print the entire response
    print("=== FULL RAW DATA ===")
    print(json.dumps(data, indent=4))

    print("\n=== BREAKDOWN CHECK ===")
    for item in data:
        if item.get('type') == "0x1::dkg::DKGState":
            last_completed = item['data'].get('last_completed', {}).get('vec', [])
            in_progress = item['data'].get('in_progress', {}).get('vec', [])

            print(f"\nLast Completed Vec Length: {len(last_completed)}")
            print("Last Completed Contents:", last_completed)
            print(f"In Progress Vec Length: {len(in_progress)}")
            print("In Progress Contents:", in_progress)
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
