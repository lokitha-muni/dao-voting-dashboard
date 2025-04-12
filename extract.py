import json

# Step 1: Load data from the previously saved response_data.json
with open("response_data.json", "r") as f:
    data = json.load(f)

# Step 2: Extract dealer_epoch from last_completed
dkg_state = data[0]
last_completed = dkg_state["data"]["last_completed"]["vec"]

if last_completed:
    dealer_epoch = last_completed[0]["metadata"]["dealer_epoch"]
else:
    dealer_epoch = None

# Step 3: Save the extracted value to a new file
output = {"dealer_epoch": dealer_epoch}

with open("new_data_file.json", "w") as f:
    json.dump(output, f, indent=4)

print("✅ Dealer epoch saved to new_data_file.json")

