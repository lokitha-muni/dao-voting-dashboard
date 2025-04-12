import dash
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
import plotly.express as px
import random

# Generate mock DAO voting data
def fetch_voting_data():
    years = [2021, 2022, 2023]
    dao_names = ["DAO1", "DAO2", "DAO3", "DAO4", "DAO5"]
    categories = ["DeFi", "NFT", "Gaming", "Infrastructure", "Governance"]
    data = []

    for year in years:
        for dao in dao_names:
            for category in categories:
                total_votes = random.randint(100, 1000)
                male_votes = random.randint(0, total_votes)
                female_votes = total_votes - male_votes
                proposals = random.randint(5, 15)
                data.append({
                    "dao_name": dao,
                    "votes": total_votes,
                    "year": year,
                    "category": category,
                    "proposals": proposals,
                    "participation_rate": round(random.uniform(40, 90), 2),
                    "male_votes": male_votes,
                    "female_votes": female_votes
                })
    return {"proposals": data}  # Wrap in dict to mimic API-style response

# Initialize Dash app
app = dash.Dash(__name__)

# Fetch data (use mock data temporarily)
data = fetch_voting_data()

# Ensure data is not empty or None
if data and "proposals" in data:
    df = pd.DataFrame(data["proposals"])

    app.layout = html.Div([
        html.H1("DAO Voting Pattern Analyzer", style={'textAlign': 'center'}),

        # Filters
        html.Div([
            html.Div([
                html.Label("Filter by Year"),
                dcc.Dropdown(
                    id='year-filter',
                    options=[{"label": y, "value": y} for y in sorted(df['year'].unique())],
                    multi=True,
                    value=sorted(df['year'].unique())
                )
            ], style={'width': '30%', 'display': 'inline-block', 'padding': '0 10px'}),

            html.Div([
                html.Label("Filter by Category"),
                dcc.Dropdown(
                    id='category-filter',
                    options=[{"label": c, "value": c} for c in sorted(df['category'].unique())],
                    multi=True,
                    value=sorted(df['category'].unique())
                )
            ], style={'width': '30%', 'display': 'inline-block', 'padding': '0 10px'}),

            html.Div([
                html.Label("Filter by Gender"),
                dcc.Dropdown(
                    id='gender-filter',
                    options=[
                        {"label": "All", "value": "All"},
                        {"label": "Male", "value": "Male"},
                        {"label": "Female", "value": "Female"}
                    ],
                    value="All",
                    clearable=False
                )
            ], style={'width': '30%', 'display': 'inline-block', 'padding': '0 10px'}),
        ], style={'padding': '20px'}),

        # KPI Cards
        html.Div(id='kpi-cards', style={'display': 'flex', 'justifyContent': 'space-around', 'padding': '20px'}),

        # Charts
        html.Div([
            html.Div([
                dcc.Graph(id='donut-participation')
            ], style={'width': '32%', 'display': 'inline-block'}),

            html.Div([
                dcc.Graph(id='bar-votes')
            ], style={'width': '32%', 'display': 'inline-block'}),

            html.Div([
                dcc.Graph(id='line-trend')
            ], style={'width': '32%', 'display': 'inline-block'}),
        ]),

        html.Div([
            dcc.Graph(id='key-metrics-trend')
        ], style={'padding': '20px'}),

        # Data Table
        html.Div([
            html.H3("Detailed DAO Proposal Data"),
            dash_table.DataTable(
                id='proposal-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'center', 'padding': '5px'},
                style_header={'fontWeight': 'bold', 'backgroundColor': '#f2f2f2'},
                page_size=10
            )
        ], style={'padding': '20px'})
    ])

    # Callback
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
        dff = df[df['year'].isin(years) & df['category'].isin(categories)]

        if gender == "Male":
            dff = dff.assign(votes=dff['male_votes'])
        elif gender == "Female":
            dff = dff.assign(votes=dff['female_votes'])

        total_votes = dff['votes'].sum()
        total_proposals = dff['proposals'].sum()
        avg_participation = round(dff['participation_rate'].mean(), 2)
        male_ratio = round((dff['male_votes'].sum() / dff[['male_votes', 'female_votes']].sum().sum()) * 100, 2)
        female_ratio = 100 - male_ratio

        kpi_cards = [
            html.Div([
                html.H4("Total Votes"), html.H2(f"{total_votes}")
            ], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
            html.Div([
                html.H4("Total Proposals"), html.H2(f"{total_proposals}")
            ], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
            html.Div([
                html.H4("Avg Participation Rate"), html.H2(f"{avg_participation}%")
            ], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
            html.Div([
                html.H4("Male vs Female"), html.H2(f"{male_ratio}% / {female_ratio}%")
            ], style={'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '10px', 'width': '20%', 'textAlign': 'center'}),
        ]

        donut = px.pie(names=["Male", "Female"], values=[dff['male_votes'].sum(), dff['female_votes'].sum()],
                       hole=0.5, title="Participation by Gender")

        bar = px.bar(dff, x='dao_name', y='votes', color='category', barmode='group', title="Votes per DAO")

        line = px.line(dff, x='year', y='votes', color='dao_name', markers=True, title="Voting Trend Over Years")

        trend_df = dff.groupby('year', as_index=False).agg({
            'participation_rate': 'mean',
            'proposals': 'sum'
        })
        trend = px.line(trend_df, x='year', y=['participation_rate', 'proposals'], markers=True,
                        title="Trend by Key Metrics")

        return kpi_cards, donut, bar, line, trend, dff.to_dict('records')

else:
    app.layout = html.Div([
        html.H1("No Data Available"),
        html.P("Unable to fetch voting data from the API.")
    ])

# Run app
if __name__ == '__main__':
    app.run(debug=True)
