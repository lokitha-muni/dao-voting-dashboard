import requests
import json

# Governance module address
address = "0x1"
event_handle = "0x1::aptos_governance::Governance"
field_name = "create_proposal_events"

# URL to fetch the events (this is the real one!)
url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{address}/events/{event_handle}/{field_name}?limit=10"

response = requests.get(url)

if response.status_code == 200:
    events = response.json()
    print("✅ Governance Proposals (sample):\n")
    print(json.dumps(events, indent=4))
else:
    print("❌ Error fetching proposal events:", response.status_code)
    print(response.text)
