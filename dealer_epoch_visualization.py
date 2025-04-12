import matplotlib.pyplot as plt
import seaborn as sns

# Example data: Dealer Epochs and their Frequencies
epochs = {
    '11004': 1,
    '11005': 3,
    '11006': 2,
    '11007': 5,
    '11008': 4,
}

# Create a bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x=list(epochs.keys()), y=list(epochs.values()))

# Add titles and labels
plt.title('Dealer Epoch Frequency', fontsize=16)
plt.xlabel('Dealer Epoch', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Show the plot
plt.show()
