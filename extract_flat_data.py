import json
import pandas as pd

# Load the JSON file
with open('response_data.json', 'r') as f:
    data = json.load(f)

# Extract meaningful entries
records = []
for item in data:
    # Get top-level type
    entry_type = item.get('type', '')

    # Get last_completed dealer_epoch if it exists
    dealer_epoch = ''
    try:
        dealer_epoch = item['data']['last_completed']['vec'][0]['metadata']['dealer_epoch']
    except (KeyError, IndexError, TypeError):
        dealer_epoch = 'N/A'

    # Add a cleaned-up row
    records.append({
        'type': entry_type,
        'dealer_epoch': dealer_epoch,
    })

# Convert to DataFrame
df = pd.DataFrame(records)

# Export to Excel
df.to_excel('flattened_dao_data.xlsx', index=False)

print("Data flattened and saved to 'flattened_dao_data.xlsx'")
