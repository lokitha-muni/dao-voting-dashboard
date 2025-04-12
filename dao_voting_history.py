import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load JSON data
with open('response_data.json', 'r') as f:
    data = json.load(f)

# Normalize JSON into a flat table
df = pd.json_normalize(data)

# Group by 'type' to see proposal activity across DAOs
dao_counts = df['type'].value_counts().reset_index()
dao_counts.columns = ['DAO_Type', 'Proposal_Count']

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(data=dao_counts, x='DAO_Type', y='Proposal_Count', palette='pastel')
plt.xticks(rotation=45, ha='right')
plt.title('Number of Proposals per DAO')
plt.xlabel('DAO Type')
plt.ylabel('Number of Proposals')
plt.tight_layout()
plt.savefig('dao_voting_history.png')
plt.show()
