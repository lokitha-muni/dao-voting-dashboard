import json

# Load the previously saved data (DAO resources data)
with open("response_data.json", "r") as file:
    dao_data = json.load(file)

# Iterate through the data and check for voting-related information
for entry in dao_data:
    if "voting" in entry.get("type", ""):  # Check if 'voting' is in the type
        # Extract the relevant voting data
        voting_data = entry  # This assumes 'entry' contains the relevant data
        
        # Save the extracted voting data to a new file
        with open("response_data.json", "w") as voting_file:
            json.dump(voting_data, voting_file, indent=4)

        print("Voting data saved to response_data.json")
