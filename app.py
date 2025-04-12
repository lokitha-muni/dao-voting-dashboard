import random
import pandas as pd
from dash import Dash, html, dcc, dash_table
import plotly.express as px

# List of actual DAO names from the Aptos ecosystem
dao_names = [
    'Spooks DAO',
    'Jungle DAO',
    'Aptomingos DAO',
    'Pontem Space Pirates DAO',
    'Lemur Lounge DAO',
    'AptoRobos DAO',
    'Mavrik DAO',
    'OrderDAO',
    'AptoSea DAO',
    'Thala Protocol DAO'
]

# Generate mock data for 100 records
def generate_mock_data(num_records=100):
    data = []
    for _ in range(num_records):
        addr = f'0x{random.randint(10**15, 10**16 - 1):x}'
        voting_power = random.randint(1, 100)
        creation_num = random.randint(1, 50)
        dao = random.choice(dao_names)
        participation_count = random.randint(0, 20)
        data.append({
            'addr': addr,
            'voting_power': voting_power,
            'creation_num': creation_num,
            'dao': dao,
            'participation_count': participation_count
        })
    return pd.DataFrame(data)

# Create DataFrame
df = generate_mock_data()

# Create figures with a light color template
fig_pie = px.pie(df, names='dao', title='DAO Participation Distribution', template='plotly_white')
fig_bar = px.bar(df, x='dao', y='voting_power', title='Voting Power by DAO', color='dao', template='plotly_white')
fig_donut = px.pie(df, names='dao', values='participation_count', hole=0.4, title='Participation Count per DAO', template='plotly_white')
fig_line = px.line(df.groupby('creation_num').sum(numeric_only=True).reset_index(),
                   x='creation_num', y='voting_power', title='Voting Power Over Time (by Creation Number)', template='plotly_white')

# Initialize Dash app
app = Dash(__name__)
app.title = "DAO Voting Dashboard"

app.layout = html.Div([
    html.H1("DAO Voting Pattern Analyzer Dashboard", style={'textAlign': 'center'}),

    html.Div([
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns],
            style_table={'overflowX': 'auto'},
            page_size=10,
            style_cell={'textAlign': 'left', 'padding': '10px'},
            style_header={'backgroundColor': '#f9f9f9', 'fontWeight': 'bold'},
        )
    ], style={'padding': '20px'}),

    html.Div([
        dcc.Graph(figure=fig_pie),
        dcc.Graph(figure=fig_donut)
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'}),

    html.Div([
        dcc.Graph(figure=fig_bar),
        dcc.Graph(figure=fig_line)
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'})
])

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
