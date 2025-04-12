import json

# Load the data from the saved JSON file
with open('response_data.json', 'r') as file:
    data = json.load(file)

# Print to check the structure of the data
print(data)
