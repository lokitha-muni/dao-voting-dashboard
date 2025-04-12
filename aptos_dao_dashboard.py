# aptos_dao_dashboard.py
import requests
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# --- Step 1: Fetch DAO Voting Data ---

def fetch_voting_data():
    # Replace this with the real DAO address you're analyzing
    dao_address = "0x1"  # Aptos governance address (example)
    url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{dao_address}/resources"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# --- Step 2: Process the Data ---

def process_data(raw_data):
    # Dummy processing since the actual voting data format depends on the API
    # Here we'll simulate with example data
    sample_data = {
        "DAOs": ["Alpha", "Beta", "Gamma", "Delta"],
        "Votes Cast": [120, 85, 150, 60],
        "Participation Rate": [75, 50, 90, 30]
    }
    df = pd.DataFrame(sample_data)
    return df

# --- Step 3: Create Dash App and Visualizations ---
raw_data = fetch_voting_data()
df = process_data(raw_data)

app = dash.Dash(__name__)
app.title = "Aptos DAO Voting Analysis"

# Pie chart: Vote Distribution by DAO
pie_chart = px.pie(
    df,
    names="DAOs",
    values="Votes Cast",
    title="Votes Cast Distribution Across DAOs"
)

# Bar chart: Participation Rate by DAO
bar_chart = px.bar(
    df,
    x="DAOs",
    y="Participation Rate",
    title="Participation Rate per DAO",
    labels={"Participation Rate": "% Participation"},
    color="DAOs"
)

app.layout = html.Div(style={"padding": "20px"}, children=[
    html.H1("DAO Voting Pattern Analysis", style={"textAlign": "center"}),
    dcc.Graph(figure=pie_chart),
    dcc.Graph(figure=bar_chart),
])

if __name__ == '__main__':
    app.run(debug=True)
