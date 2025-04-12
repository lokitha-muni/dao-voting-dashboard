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

# Create a pie chart
plt.figure(figsize=(7, 7))
plt.pie(epochs.values(), labels=epochs.keys(), autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))

# Add a title
plt.title('Dealer Epoch Proportions', fontsize=16)

# Show the plot
plt.show()
