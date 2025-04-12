import json
import matplotlib.pyplot as plt

# Step 1: Load the data from the JSON file
with open('epoch_frequency.json', 'r') as file:
    epoch_count = json.load(file)

# Step 2: Extract epochs and frequencies into lists
epochs = list(epoch_count.keys())
frequencies = list(epoch_count.values())

# Step 3: Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(epochs, frequencies, color='skyblue')

# Add titles and labels
plt.title('Frequency of Dealer Epochs')
plt.xlabel('Dealer Epoch')
plt.ylabel('Frequency')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Adjust layout to fit labels
plt.tight_layout()

# Show the plot
plt.show()
