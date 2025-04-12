import json

# Assuming 'data' contains the response and it has sets in it
data = [{"type": "0x1::dkg::DKGState", "data": {"in_progress": {"vec": []}, "last_completed": {"vec": [{"metadata": {"dealer_epoch": "11004"}}]}}}]  # Example data with sets in it.

# Function to recursively convert sets to lists in the data
def convert_sets_to_lists(obj):
    if isinstance(obj, dict):
        return {key: convert_sets_to_lists(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_sets_to_lists(item) for item in obj]
    elif isinstance(obj, set):
        return list(obj)  # Convert set to list
    else:
        return obj

# Convert sets to lists in the data
data = convert_sets_to_lists(data)

# Now save it to a JSON file
with open("fixed_data_file.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data saved to response_data.json")
