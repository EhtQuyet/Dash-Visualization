import pathlib
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Output, Input

from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("bank.csv"))

layout = html.Div([
    html.H1("Graph Analysis with Banking Data"),
    dcc.Dropdown(id='job-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.job.unique())],
                 value='admin.',
                 style={'width': '50%'}
                 ),
    dcc.Dropdown(id='marital-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.marital.unique())],
                 value='married',
                 style={'width': '50%'}
                 ),
    dcc.Graph(id='bank-bar-graph',
              figure={}),
])


@app.callback(
    Output(component_id='bank-bar-graph', component_property='figure'),
    Input(component_id='job-choice', component_property='value'),
    Input(component_id='marital-choice', component_property='value')
)
def interactive_graphs(value_job, value_marital):
    dff = df[df.job == value_job]
    dff = dff[dff.marital == value_marital]
    fig = px.bar(data_frame=dff, x='month', y='balance')
    return fig
