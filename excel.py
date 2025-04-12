import json
import pandas as pd

# Load the JSON file
with open('response_data.json', 'r') as f:
    data = json.load(f)

# Flatten nested fields properly
df = pd.json_normalize(data, sep='_')

# Export clean Excel
df.to_excel('dao_data_output_cleaned.xlsx', index=False)

print("✅ Cleaned data exported to 'dao_data_output_cleaned.xlsx'")
