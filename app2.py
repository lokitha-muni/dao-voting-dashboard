import dash
from dash import dcc, html, dash_table, Input, Output, State
import pandas as pd
import plotly.express as px
import random
import base64
import io

# Initialize Dash app
app = dash.Dash(__name__)

# Initialize a global variable to hold the dataframe
df = pd.DataFrame()

# Layout with file upload feature
app.layout = html.Div([
    html.H1("DAO Voting Pattern Analyzer", style={'textAlign': 'center'}),

    # File upload
    dcc.Upload(
        id='upload-data',
        children=html.Button('Upload CSV'),
        multiple=False
    ),
    
    # Filters
    html.Div([
        html.Div([
            html.Label("Filter by Year"),
            dcc.Dropdown(id='year-filter', multi=True),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '0 10px'}),

        html.Div([
            html.Label("Filter by Category"),
            dcc.Dropdown(id='category-filter', multi=True),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '0 10px'}),

        html.Div([
            html.Label("Filter by Gender"),
            dcc.Dropdown(id='gender-filter', value="All", clearable=False),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '0 10px'}),
    ], style={'padding': '20px'}),

    # KPI Cards
    html.Div(id='kpi-cards', style={'display': 'flex', 'justifyContent': 'space-around', 'padding': '20px'}),

    # Charts
    html.Div([
        html.Div([dcc.Graph(id='donut-participation')], style={'width': '32%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(id='bar-votes')], style={'width': '32%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(id='line-trend')], style={'width': '32%', 'display': 'inline-block'}),
    ]),

    # Trend Metrics
    html.Div([dcc.Graph(id='key-metrics-trend')], style={'padding': '20px'}),

    # Data Table
    html.Div([html.H3("Detailed DAO Proposal Data"),
              dash_table.DataTable(id='proposal-table', style_table={'overflowX': 'auto'},
                                   style_cell={'textAlign': 'center', 'padding': '5px'},
                                   style_header={'fontWeight': 'bold', 'backgroundColor': '#f2f2f2'},
                                   page_size=10)
              ], style={'padding': '20px'})
])


# Parse CSV content and update dataframe
def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        # Try to read CSV
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        return df
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return pd.DataFrame()


# Callback for file upload
@app.callback(
    [Output('year-filter', 'options'),
     Output('category-filter', 'options'),
     Output('gender-filter', 'options'),
     Output('kpi-cards', 'children'),
     Output('donut-participation', 'figure'),
     Output('bar-votes', 'figure'),
     Output('line-trend', 'figure'),
     Output('key-metrics-trend', 'figure'),
     Output('proposal-table', 'data')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def update_data(contents, filename):
    global df
    if contents is None:
        return dash.no_update  # Don't update if no file uploaded

    # Parse the contents of the uploaded file
    df = parse_contents(contents)

    if df.empty:
        return dash.no_update

    # Update the filter options based on the CSV data
    year_options = [{"label": str(year), "value": year} for year in sorted(df['year'].unique())]
    category_options = [{"label": category, "value": category} for category in sorted(df['category'].unique())]
    gender_options = [
        {"label": "All", "value": "All"},
        {"label": "Male", "value": "Male"},
        {"label": "Female", "value": "Female"}
    ]
    
    # Callback logic to update KPI cards and charts
    total_votes = df['votes'].sum()
    total_proposals = df['proposals'].sum()
    avg_participation = round(df['participation_rate'].mean(), 2)
    male_ratio = round((df['male_votes'].sum() / df[['male_votes', 'female_votes']].sum().sum()) * 100, 2)
    female_ratio = 100 - male_ratio

    kpi_cards = [
        html.Div([html.H4("Total Votes"), html.H2(f"{total_votes}")], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
        html.Div([html.H4("Total Proposals"), html.H2(f"{total_proposals}")], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
        html.Div([html.H4("Avg Participation Rate"), html.H2(f"{avg_participation}%")], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
        html.Div([html.H4("Male vs Female"), html.H2(f"{male_ratio}% / {female_ratio}%")], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
    ]

    donut = px.pie(names=["Male", "Female"], values=[df['male_votes'].sum(), df['female_votes'].sum()], hole=0.5, title="Participation by Gender")
    bar = px.bar(df, x='dao_name', y='votes', color='category', barmode='group', title="Votes per DAO")
    line = px.line(df, x='year', y='votes', color='dao_name', markers=True, title="Voting Trend Over Years")

    trend_df = df.groupby('year', as_index=False).agg({
        'participation_rate': 'mean',
        'proposals': 'sum'
    })
    trend = px.line(trend_df, x='year', y=['participation_rate', 'proposals'], markers=True, title="Trend by Key Metrics")

    return year_options, category_options, gender_options, kpi_cards, donut, bar, line, trend, df.to_dict('records')


import os

# For deployment, bind to PORT from environment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))  # fallback to 8050 for local
    app.run(host="0.0.0.0", port=port)

