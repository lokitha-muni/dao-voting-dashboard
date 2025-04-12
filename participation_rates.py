import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load JSON data
with open('response_data.json', 'r') as f:
    data = json.load(f)

# Normalize JSON
df = pd.json_normalize(data)

# Check which columns are available
print("Available columns:", df.columns.tolist())

# If a column like 'in_progress_completed.vcec' contains 'voters', extract from there
# We'll look for it safely using apply and try/except

def extract_voter_count(row):
    try:
        proposal_data = row['in_progress_completed.vcec']
        if isinstance(proposal_data, list) and len(proposal_data) > 0:
            metadata = proposal_data[0].get('metadata', {})
            return int(metadata.get('voter_count', 0))  # Adjust if structure is different
    except Exception:
        return 0
    return 0

df['voter_count'] = df.apply(extract_voter_count, axis=1)

# Group by DAO type and calculate average participation
participation = df.groupby('type')['voter_count'].mean().reset_index()
participation.columns = ['DAO_Type', 'Average_Voter_Count']

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=participation, x='DAO_Type', y='Average_Voter_Count', palette='muted')
plt.xticks(rotation=45, ha='right')
plt.title('Average Voter Participation per DAO')
plt.xlabel('DAO Type')
plt.ylabel('Average Voter Count')
plt.tight_layout()
plt.savefig('dao_participation_rates.png')
plt.show()

