import json

# Load the wrong version (stringified JSON)
with open("new_data_file.json", "r") as f:
    raw = f.read()
    actual_data = json.loads(raw)  # Convert string to actual JSON (list/dict)

# Save it correctly as a proper JSON file
with open("fixed_data_file.json", "w") as f:
    json.dump(actual_data, f, indent=4)

print("✅ Fixed JSON saved as 'fixed_data_file.json'")
