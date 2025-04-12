import requests
import json

# Pontem DAO address (real Aptos DAO)
dao_address = "0x7e60df042a9f87fe"

# Aptos REST API URL to get resources
url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{dao_address}/resources"

# Make request
response = requests.get(url)

if response.status_code == 200:
    resources = response.json()
    print("✅ Pontem DAO Resources:\n")
    for r in resources[:5]:  # Show first 5 only
        print(json.dumps(r, indent=4), "\n---\n")
else:
    print("❌ Error fetching DAO resources:", response.status_code)
    print(response.text)
