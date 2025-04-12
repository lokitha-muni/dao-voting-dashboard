import requests
import json

# This is a system address with real on-chain events
address = "0x1"
event_handle = "0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>"
field_name = "withdraw_events"

url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{address}/events/{event_handle}/{field_name}?limit=3"

response = requests.get(url)

if response.status_code == 200:
    print("✅ Success! Sample event data:\n")
    print(json.dumps(response.json(), indent=4))
else:
    print("❌ Failed:", response.status_code)
    print(response.text)
