import json

# Your extracted value
dealer_epoch = "11004"

# Save as a list (you can add more later)
dealer_epochs = [dealer_epoch]

# Save to new file
with open("dealer_epochs.json", "w") as f:
    json.dump(dealer_epochs, f, indent=4)

print("✅ Saved dealer epochs to dealer_epochs.json")
