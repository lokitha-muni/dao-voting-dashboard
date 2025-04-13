# fetch_data.py
import requests
import pandas as pd

def fetch_voting_data():
    dao_address = "0x1"  # Aptos Governance address (example)
    url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{dao_address}/resources"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        dao_data = [res for res in data if "Voting" in res.get("type", "")]
        if not dao_data:
            print("No DAO voting data found.")
            return pd.DataFrame()

        # Sample mock structure (you may need to adjust based on real API)
        records = []
        for item in dao_data:
            inner = item["data"]
            records.append({
                "voter": inner.get("voter_address", "N/A"),
                "proposal_id": inner.get("proposal_id", "N/A"),
                "vote": inner.get("vote", "N/A"),
                "timestamp": inner.get("timestamp", 0)
            })

        df = pd.DataFrame(records)
        return df
    except requests.exceptions.RequestException as e:
        print("❌ Failed to fetch data:", e)
        return pd.DataFrame()
