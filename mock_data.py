# mock_data.py

import json

# Mock data that simulates the actual API response.
mock_data = {
    "proposals": [
        {
            "id": 1,
            "title": "Proposal 1",
            "voting_power": 5000,
            "voting_history": [0, 1, 0, 1],
            "participation_rate": 0.8,
        },
        {
            "id": 2,
            "title": "Proposal 2",
            "voting_power": 6000,
            "voting_history": [1, 1, 0, 1],
            "participation_rate": 0.9,
        },
        {
            "id": 3,
            "title": "Proposal 3",
            "voting_power": 2000,
            "voting_history": [0, 1, 1, 0],
            "participation_rate": 0.7,
        },
        {
            "id": 4,
            "title": "Proposal 4",
            "voting_power": 3000,
            "voting_history": [1, 1, 1, 1],
            "participation_rate": 1.0,
        },
        # Add more proposals as needed...
    ]
}

# Save the mock data to a JSON file to simulate an API response.
with open("mock_proposals.json", "w") as outfile:
    json.dump(mock_data, outfile)
    
print("Mock data saved to 'mock_proposals.json'.")
