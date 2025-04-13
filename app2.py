import dash
from dash import dcc, html, dash_table, Input, Output, State
import pandas as pd
import plotly.express as px
import random
import base64
import io
import os

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "DAO Voting Pattern Analyzer"

# Initialize a global variable to hold the dataframe
df = pd.DataFrame()

# Layout
app.layout = html.Div([
    html.H1("DAO Voting Pattern Analyzer", style={'textAlign': 'center'}),

    dcc.Upload(
        id='upload-data',
        children=html.Button('Upload CSV'),
        multiple=False
    ),

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

    html.Div(id='kpi-cards', style={'display': 'flex', 'justifyContent': 'space-around', 'padding': '20px'}),

    html.Div([
        html.Div([dcc.Graph(id='donut-participation')], style={'width': '32%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(id='bar-votes')], style={'width': '32%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(id='line-trend')], style={'width': '32%', 'display': 'inline-block'}),
    ]),

    html.Div([dcc.Graph(id='key-metrics-trend')], style={'padding': '20px'}),

    html.Div([html.H3("Detailed DAO Proposal Data"),
              dash_table.DataTable(id='proposal-table',
                                   style_table={'overflowX': 'auto'},
                                   style_cell={'textAlign': 'center', 'padding': '5px'},
                                   style_header={'fontWeight': 'bold', 'backgroundColor': '#f2f2f2'},
                                   page_size=10)
              ], style={'padding': '20px'})
])

# Parse uploaded CSV
def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        return df
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return pd.DataFrame()

# File Upload Callback: Sets dropdown options only
@app.callback(
    [Output('year-filter', 'options'),
     Output('category-filter', 'options'),
     Output('gender-filter', 'options')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def update_filter_options(contents, filename):
    global df
    if contents is None:
        return dash.no_update, dash.no_update, dash.no_update

    df = parse_contents(contents)
    if df.empty:
        return [], [], []

    year_options = [{"label": str(year), "value": year} for year in sorted(df['year'].unique())]
    category_options = [{"label": cat, "value": cat} for cat in sorted(df['category'].unique())]
    gender_options = [
        {"label": "All", "value": "All"},
        {"label": "Male", "value": "Male"},
        {"label": "Female", "value": "Female"}
    ]

    return year_options, category_options, gender_options

# Second Callback: Updates charts, KPIs, and table based on filters
@app.callback(
    [Output('kpi-cards', 'children'),
     Output('donut-participation', 'figure'),
     Output('bar-votes', 'figure'),
     Output('line-trend', 'figure'),
     Output('key-metrics-trend', 'figure'),
     Output('proposal-table', 'data')],
    [Input('year-filter', 'value'),
     Input('category-filter', 'value'),
     Input('gender-filter', 'value')]
)
def update_dashboard(years, categories, gender):
    if df.empty:
        return [html.Div("No data uploaded yet.")]*6

    filtered_df = df.copy()

    if years:
        filtered_df = filtered_df[filtered_df['year'].isin(years)]
    if categories:
        filtered_df = filtered_df[filtered_df['category'].isin(categories)]
    if gender and gender != "All":
        if gender == "Male":
            filtered_df = filtered_df[filtered_df['male_votes'] > 0]
        elif gender == "Female":
            filtered_df = filtered_df[filtered_df['female_votes'] > 0]

    total_votes = filtered_df['votes'].sum()
    total_proposals = filtered_df['proposals'].sum()
    avg_participation = round(filtered_df['participation_rate'].mean(), 2) if not filtered_df.empty else 0
    male_ratio = round((filtered_df['male_votes'].sum() / (filtered_df[['male_votes', 'female_votes']].sum().sum())) * 100, 2) if filtered_df[['male_votes', 'female_votes']].sum().sum() > 0 else 0
    female_ratio = 100 - male_ratio

    kpi_cards = [
        html.Div([html.H4("Total Votes"), html.H2(f"{total_votes}")], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
        html.Div([html.H4("Total Proposals"), html.H2(f"{total_proposals}")], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
        html.Div([html.H4("Avg Participation Rate"), html.H2(f"{avg_participation}%")], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
        html.Div([html.H4("Male vs Female"), html.H2(f"{male_ratio}% / {female_ratio}%")], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
    ]

    donut = px.pie(names=["Male", "Female"], values=[filtered_df['male_votes'].sum(), filtered_df['female_votes'].sum()], hole=0.5, title="Participation by Gender")
    bar = px.bar(filtered_df, x='dao_name', y='votes', color='category', barmode='group', title="Votes per DAO")
    line = px.line(filtered_df, x='year', y='votes', color='dao_name', markers=True, title="Voting Trend Over Years")

    trend_df = filtered_df.groupby('year', as_index=False).agg({
        'participation_rate': 'mean',
        'proposals': 'sum'
    })
    trend = px.line(trend_df, x='year', y=['participation_rate', 'proposals'], markers=True, title="Trend by Key Metrics")

    return kpi_cards, donut, bar, line, trend, filtered_df.to_dict('records')

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port)
