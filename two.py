import requests
import json

dao_address = "0x9d8b90f7a607aa53844b3c431abe95f0b17919f1fe5359a18964a04b0a8324b0"
url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{dao_address}/resources"

response = requests.get(url)

if response.status_code == 200:
    resources = response.json()
    print("✅ DAO Resources:\n")
    print(json.dumps(resources, indent=4))
else:
    print("❌ Error fetching DAO resources:", response.status_code)
    print(response.text)
