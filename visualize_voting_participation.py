import json
import matplotlib.pyplot as plt

# Load the response data
with open('response_data.json', 'r') as file:
    response_data = json.load(file)

# Extract vote participation data
voting_participation = []
for entry in response_data:
    if "data" in entry and "events" in entry["data"]:
        vote_data = entry["data"]["events"].get("vote_events", {})
        voting_participation.append(vote_data.get("counter", 0))

# Plot the voting participation
plt.figure(figsize=(10, 6))
plt.plot(range(len(voting_participation)), voting_participation, marker='x', linestyle='-', color='red')
plt.xlabel('Epochs')
plt.ylabel('Voting Participation')
plt.title('Voting Participation Across Epochs')
plt.tight_layout()
plt.show()
