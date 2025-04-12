import json

# Load the saved data
with open('dealer_epochs.json', 'r') as file:
    data = json.load(file)

# Print out the data for review
print("Dealer Epochs:")
for epoch in data:
    print(f"Epoch: {epoch}")

# Count occurrences of each epoch
epoch_count = {}
for epoch in data:
    if epoch in epoch_count:
        epoch_count[epoch] += 1
    else:
        epoch_count[epoch] = 1

print("\nEpoch Frequency:")
for epoch, count in epoch_count.items():
    print(f"Epoch {epoch}: {count} times")
