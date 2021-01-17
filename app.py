# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://richard-gm.github.io/dash_data_analysis/data/results_2020.csv')


fig = px.scatter(df,
                 x="Time",
                 y="Result (GBP)",
                 title='My Trading212 account',
                 color="Ticker")

app.layout = html.Div([
    dcc.Graph(
        id='td212account',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

# TODO Add new column based on new condition for size scatter parameter.
# Eg if resultGBP is > 50 then 1... etc.
