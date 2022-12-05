import pathlib
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Output, Input

from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("excel_dash.csv"))

layout = html.Div([
    html.H1("Graph Analysis with Charming Data"),
    dcc.Dropdown(id='genre-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.Genre.unique())],
                 value='Action',
                 style={'width': '50%'}
                 ),
    dcc.Dropdown(id='platform-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.Platform.unique())],
                 value='PS4',
                 style={'width': '50%'}
                 ),
    dcc.Graph(id='my-graph',
              figure={}),
])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='genre-choice', component_property='value'),
    Input(component_id='platform-choice', component_property='value')
)
def interactive_graphs(value_genre, value_platform):
    dff = df[df.Genre == value_genre]
    dff = dff[dff.Platform == value_platform]
    fig = px.bar(data_frame=dff, x='Year', y='Japan Sales')
    return fig
