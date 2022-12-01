import pathlib

import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
# Connect to your app pages
from apps import practice, data_table

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("iranian_students.csv"))

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Number of students per education level", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Graph Analysis", href="/", active="exact"),
                dbc.NavLink("Data Table", href="/data-table", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    content,
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname == "/":
        return practice.layout
    elif pathname == "/data-table":
        return data_table.layout
    elif pathname == "/page-2":
        "404 Page Error! Please choose a link"
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=False)
