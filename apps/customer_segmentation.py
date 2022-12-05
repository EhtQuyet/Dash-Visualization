import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import dash  # (version 1.9.1) pip install dash==1.9.1
from dash import dcc, html, Input, Output
import pathlib
from app import app
from dash import dash_table

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_excel(DATA_PATH.joinpath("data.xlsx"))

df_not_nan = df[df['CustomerID'].notna()]
df_not_nan = df_not_nan.sample(10000, random_state=42)
df_not_nan.head(10)

layout = dash_table.DataTable(
    data=df_not_nan.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    style_table={'height': '400px', 'overflowY': 'auto'},
    page_action='native',  # all data is passed to the table up-front
    page_size=10,  # only 10 rows are displayed at a time
    fixed_rows={'headers': True},

)

