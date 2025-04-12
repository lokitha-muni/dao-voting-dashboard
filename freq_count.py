import json

# Example data: this would be your retrieved data
dealer_epochs = [11004, 11004, 11005, 11006, 11004]  # Add your list of dealer epochs here

# Count the frequency of each epoch
epoch_count = {}
for epoch in dealer_epochs:
    if epoch in epoch_count:
        epoch_count[epoch] += 1
    else:
        epoch_count[epoch] = 1

# Save the epoch frequency count to a new JSON file
with open('epoch_frequency.json', 'w') as file:
    json.dump(epoch_count, file, indent=4)

print("Epoch frequency saved to 'epoch_frequency.json'")
