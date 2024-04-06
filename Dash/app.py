from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


def serve_layout():
    return html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
        Dash: A web application framework for your data.
    '''),
        html.Div([dcc.Graph(id='example-graph',figure=fig)]),
        html.Div(
            children=[
                html.P(children=[
                    "Last Updated: ",
                    html.Span(id='time',children=["hello"]),
                ]),
                html.P("Please email the digitalization team with any errors that you find including a screenshot"),
                dcc.Dropdown(
                    id='main-viewer',
                    options=[
                        {'label': 'Area-Adjusted', 'value': 'Area'},
                        {'label': 'APO', 'value': 'APO'}
                    ],
                    value='Area'
                ),
            ]
        ),
    ])


external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets,
           suppress_callback_exceptions=True)
app.layout = serve_layout()


@app.callback([Output('time', 'children')],
              Input('main-viewer', 'value'))
def update_time(view):
    if view == 'APO':
        return ["helloworld"]
    else:
        return ["heihei"]


if __name__ == '__main__':
    app.run_server(debug=True)
