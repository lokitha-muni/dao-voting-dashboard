import requests
import json

# Try the correct governance endpoint
url = "https://api.mainnet.aptoslabs.com/v1/governance/proposal-history"


response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    proposals = response.json()
    print("=== PROPOSALS FOUND ===")
    for proposal in proposals:
        print("Proposal ID:", proposal.get("id"))
        print("Execution Hash:", proposal.get("execution_hash"))
        print("Expiration Timestamp:", proposal.get("expiration_timestamp_secs"))
        print("Is Resolved:", proposal.get("is_resolved"))
        print("-" * 40)
else:
    print("Error fetching proposals:", response.status_code)
    print("URL Tried:", url)
