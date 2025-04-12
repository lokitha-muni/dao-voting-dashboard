import json
import matplotlib.pyplot as plt

# Load voting forum data
with open('response_data.json', 'r') as file:
    forum_data = json.load(file)

# Extract voting forum information
vote_forums = []
for entry in forum_data:
    if "data" in entry and "events" in entry["data"]:
        vote_forums.append(entry["data"]["events"])

# Count the number of forum events
forum_event_counts = {
    "create_proposal": sum(1 for event in vote_forums if "create_proposal_events" in event),
    "register_forum": sum(1 for event in vote_forums if "register_forum_events" in event),
    "resolve_proposal": sum(1 for event in vote_forums if "resolve_proposal_events" in event),
}

# Plot the forum events
plt.figure(figsize=(10, 6))
plt.bar(forum_event_counts.keys(), forum_event_counts.values(), color='orange')
plt.xlabel('Forum Event Types')
plt.ylabel('Frequency')
plt.title('Forum Event Types Frequency')
plt.tight_layout()
plt.show()
