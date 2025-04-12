import json
import matplotlib.pyplot as plt

# Load the epoch frequency data
with open('epoch_frequency.json', 'r') as file:
    epoch_data = json.load(file)

# Extract epoch and frequency data
epochs = list(epoch_data.keys())
frequencies = list(epoch_data.values())

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(epochs, frequencies, color='skyblue')
plt.xlabel('Epochs')
plt.ylabel('Frequency')
plt.title('Frequency of Proposals per Epoch')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
