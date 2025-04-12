import json
import matplotlib.pyplot as plt

# Load dealer epoch data
with open('new_data_file.json', 'r') as file:
    dealer_epoch_data = json.load(file)

# Extract the dealer epoch
dealer_epochs = dealer_epoch_data.get("dealer_epoch", [])

# Count the frequency of each dealer epoch
epoch_count = {epoch: dealer_epochs.count(epoch) for epoch in set(dealer_epochs)}

# Plot the frequency of dealer epochs
plt.figure(figsize=(10, 6))
plt.bar(epoch_count.keys(), epoch_count.values(), color='lightgreen')
plt.xlabel('Dealer Epochs')
plt.ylabel('Frequency')
plt.title('Frequency of Dealer Epochs')
plt.tight_layout()
plt.show()
