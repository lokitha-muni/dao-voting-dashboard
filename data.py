import requests
import json

dao_address = "0x1"
url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{dao_address}/resources"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Raw Response:", response.text[:500])  # Print first 500 characters

try:
    data = response.json()
    print("\nParsed JSON Types:\n")

    for item in data:
        print(item['type'])

except json.JSONDecodeError:
    print("⚠️ Error: Couldn't decode JSON response")
except Exception as e:
    print("⚠️ Some other error:", e)
