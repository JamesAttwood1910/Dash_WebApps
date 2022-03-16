# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.read_csv('https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv')


@app.callback(
    Output('graph1', 'figure'), 
    Input('x_dropdown', 'value'),
    Input('y_dropdown', 'value')

    )

def update_figure(x_var, y_var):
    fig = px.scatter(df, x = x_var, y = y_var, title = "Scatter Plot")
    fig.update_layout(transition_duration = 1000)
    return fig

app.layout = html.Div(children=[
    html.H1(children='Welcome'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='graph1'
    ),

    html.H3('Choose X and Y variables you would like to plot.'),

    html.H4('X Variable:'),

    dcc.Dropdown(['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec',
        'vs', 'am', 'gear', 'carb'], 'mpg', id='x_dropdown'),

    html.H4('Y variable:'),

    dcc.Dropdown(['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec',
        'vs', 'am', 'gear', 'carb'], 'mpg', id='y_dropdown'),

    html.Br()
])



if __name__ == '__main__':
    app.run_server(debug=True)