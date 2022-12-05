import pathlib

import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
# Connect to your app pages
from apps import bar_genre, data_table, table_bank, bar_bank, bank_dropdown_pie_chart
from apps import  customer_segmentation, rfm

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("datasets").resolve()

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
        dbc.Nav(
            [
                dbc.NavLink("Genre Data", href="/", active="exact"),
                dbc.NavLink("Bank Data", href="/table-bank", active="exact"),
                dbc.NavLink("Bar Chart Genre", href="/graph-analysis-genre", active="exact"),
                dbc.NavLink("Bar Chart Bank", href="/graph-analysis-bank", active="exact"),
                dbc.NavLink("Pie Chart Bank", href="/pie-chart-bank", active="exact"),
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
        return customer_segmentation.layout
    elif pathname == "/table-bank":
        return table_bank.layout
    elif pathname == "/graph-analysis-genre":
        return bar_genre.layout
    elif pathname == "/graph-analysis-bank":
        return bar_bank.layout
    elif pathname == "/pie-chart-bank":
        return bank_dropdown_pie_chart.layout
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
