# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# import dash  # (version 1.9.1) pip install dash==1.9.1
# from dash import dcc, html, Input, Output
# import pathlib
# from app import app
# from dash import dash_table
# import datetime
# import dash_bootstrap_components as dbc
# import plotly.figure_factory as ff
# #
# # PATH = pathlib.Path(__file__).parent
# # DATA_PATH = PATH.joinpath("../datasets").resolve()
# # df = pd.read_excel(DATA_PATH.joinpath("data.xlsx"))
# #
# # df_not_nan = df[df['CustomerID'].notna()]
# # df_not_nan = df_not_nan.sample(10000, random_state=42)
# # df_not_nan.head(10)
# #
# # # Tinh toan RFM
# #
# # # -------- Tinh R - Recency
# #
# # # Chuyen tu string -> date
# # df_not_nan['InvoiceDate'] = pd.to_datetime(df_not_nan['InvoiceDate'], format='%Y-%m-%d %H:%M:%S')
# #
# # # Lay ngay lon nhat trong InvoiceDate + 1
# # current_date = max(df_not_nan['InvoiceDate']) + datetime.timedelta(days=1)
# #
# # # -------- Tinh M - MoneytaryValue
# # df_not_nan['TotalPay'] = df_not_nan['Quantity'] * df_not_nan['UnitPrice']
# #
# # # Group by CustomerID de tinh R, F, M
# #
# # df_customers = df_not_nan.groupby(['CustomerID']).agg(
# #     {'InvoiceDate': lambda x: (current_date - x.max()).days,
# #      'InvoiceNo': 'count',
# #      'TotalPay': 'sum'
# #      }
# # )
# # df_customers.rename(columns={'InvoiceDate': 'Recency', 'InvoiceNo': 'Frequency', 'TotalPay': 'MonetaryValue'},
# #                     inplace=True)
#
# x = np.random.randn(1000)
# hist_data = [x]
# group_labels = ['distplot']  # name of the dataset
#
# fig = ff.create_distplot(hist_data, group_labels)
#
# card_recency = dbc.Card(
#     dbc.CardBody(
#         [
#             html.H1([html.I(className="bi bi-currency-dollar me-2"), "Sales"], className="text-nowrap"),
#             html.H3("$106.7M"),
#             html.Div(
#                 [
#                     dcc.Graph(
#                         figure=fig
#                     )
#
#                 ]
#             ),
#         ], className="border-start border-success border-5"
#     ),
#     className="text-center m-4"
# )
#
# # layout = dash_table.DataTable(
# #     data=df_customers.to_dict('records'),
# #     columns=[{'id': c, 'name': c} for c in df_customers.columns],
# #     style_table={'height': '400px', 'overflowY': 'auto'},
# #     page_action='native',  # all data is passed to the table up-front
# #     page_size=10,  # only 10 rows are displayed at a time
# #     fixed_rows={'headers': True},
# #
# # )
#
# layout = dbc.Container(
#     dbc.Row(
#         [dbc.Col(card_recency)],
#     ),
#     fluid=True,
# )
