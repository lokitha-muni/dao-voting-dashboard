import requests
import pandas as pd
import sys

# Reconfigure stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Your proposal handle (from Aptos)
# Example of a known test handle (use a valid one from Aptos)

dao_address = "0x1"  # Known active address on Aptos
url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{dao_address}/resources"

# Send request to the API
response = requests.get(url)

# Check for success
if response.status_code == 200:
    data = response.json()
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Optional: Keep only useful columns if available
    columns_to_keep = ['addr', 'voting_power', 'pk_bytes']
    df = df[[col for col in columns_to_keep if col in df.columns]]
    
    # Save to Excel
    df.to_excel("dao_voting_data.xlsx", index=False)
    
    # Save to CSV (Power BI friendly)
    df.to_csv("dao_voting_data.csv", index=False)
    
    print("✅ Data exported successfully as 'dao_voting_data.xlsx' and 'dao_voting_data.csv'")
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
