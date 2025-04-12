import matplotlib.pyplot as plt
import seaborn as sns

# Example data: Dealer Epochs (Use the frequency data if needed)
epochs = [11004, 11005, 11006, 11007, 11008, 11005, 11006, 11007, 11008, 11008]

# Create a histogram
plt.figure(figsize=(8, 6))
sns.histplot(epochs, bins=5, kde=True)

# Add titles and labels
plt.title('Dealer Epoch Distribution', fontsize=16)
plt.xlabel('Dealer Epoch', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Show the plot
plt.show()
