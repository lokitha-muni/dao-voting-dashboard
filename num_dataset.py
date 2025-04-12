import requests

dao_address = "0x1"  # Known active address on Aptos
url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{dao_address}/resources"
response = requests.get(url)
response_data = response.json()  # Convert the response to a JSON object

print(response_data)  # View the full response

number_of_datasets = len(response_data)
print(f"Number of datasets retrieved: {number_of_datasets}")