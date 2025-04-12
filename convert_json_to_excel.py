import json
import pandas as pd

# Load the JSON data
with open('response_data.json', 'r') as f:
    data = json.load(f)

# Flatten the JSON structure
df = pd.json_normalize(data)

# Export to Excel (without emoji to avoid encoding errors)
df.to_excel('dao_data_output_cleaned.xlsx', index=False)

print("Data successfully exported to 'dao_data_output_cleaned.xlsx'")
