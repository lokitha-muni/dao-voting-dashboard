import json

# Load the data file
with open("fixed_data_file.json", "r") as f:
    data = json.load(f)

# Loop through and extract dealer_epoch
for entry in data:
    if isinstance(entry, dict) and "data" in entry:
        last_completed = entry["data"]["last_completed"]["vec"]
        if last_completed:
            dealer_epoch = last_completed[0]["metadata"]["dealer_epoch"]
            print("✅ Dealer epoch is:", dealer_epoch)
        else:
            print("ℹ️ No 'last_completed' entries.")
    else:
        print("❌ Entry is not a dictionary:", entry)
