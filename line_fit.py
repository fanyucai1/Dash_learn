
import plotly.graph_objs as go
# Scientific libraries
from scipy import stats
import pandas as pd
import sys
import dash
import dash_html_components as html
import dash_core_components as dcc

def run(tsv,xname,yname):
    df=pd.read_table(tsv,sep="\t",header=0)
    x=df['%s'%(xname)]
    y=df['%s'%(yname)]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    line = slope * x + intercept
    trace1 = go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=go.Marker(color='rgb(255, 127, 14)'),
        name='Data'
    )
    trace2 = go.Scatter(
        x=x,
        y=line,
        mode='lines',
        marker=go.Marker(color='rgb(31, 119, 180)'),
        name='Fit'
    )
    app = dash.Dash(__name__)
    app.layout = html.Div([
        dcc.Graph(
            figure=go.Figure(data=[trace1,trace2])
        )],id='my-graph')
    app.run_server(debug=True)

if __name__=="__main__":
    if len(sys.argv)!=4:
        print("usage:python3 input.tsv xname yname\n")
        print("Email:fanyucai1@126.com")
    else:
        run(sys.argv[1], sys.argv[2], sys.argv[3])