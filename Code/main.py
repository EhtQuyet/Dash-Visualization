from dash import Dash, dcc, html, Input, Output

import numpy as np  # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

app = Dash(__name__)

train = pd.read_csv('./data/train.csv', sep=';')
test = pd.read_csv('./data/test.csv', sep=';')

sns.set_theme(style='darkgrid')
sns.set(rc={'figure.figsize': (6, 5)})
job = sns.countplot(x="job", data=train, hue="y", order=train["job"].value_counts().index)
job.tick_params(axis='x', rotation=60)
plt.title("Bivariate analysis of the relationship between 'job' and 'y'")
avg_age_by_job = pd.DataFrame({'age': train.groupby(["job"])['age'].mean()}).reset_index()
fig = {
    "data": [
        {'x': avg_age_by_job.loc[:, 'job'], 'y': avg_age_by_job.loc[:, 'age'], 'type': 'bar'},
    ],
    'layout': {
        'title': 'Dash Data Visualization',
    }
}
app.layout = html.Div([
    dcc.Graph(figure=fig)
])


def func(n_clicks):
    return dcc.Graph(figure=fig)


if __name__ == '__main__':
    app.run_server(debug=True)
