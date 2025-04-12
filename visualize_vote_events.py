import json
import matplotlib.pyplot as plt

# Load voting events data
with open('response_data.json', 'r') as file:
    voting_data = json.load(file)

# Extract voting event data
voting_events = []
for entry in voting_data:
    if "data" in entry and "events" in entry["data"]:
        voting_events.append(entry["data"]["events"])

# Count the number of voting events
event_counts = [event.get("vote_events", {}).get("counter", 0) for event in voting_events]

# Plot the voting events
plt.figure(figsize=(10, 6))
plt.plot(range(len(event_counts)), event_counts, marker='o', linestyle='-', color='purple')
plt.xlabel('Epochs')
plt.ylabel('Number of Vote Events')
plt.title('Voting Events Across Epochs')
plt.tight_layout()
plt.show()
