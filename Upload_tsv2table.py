import base64#解码或者编码二进制
import io
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

app = dash.Dash(__name__)
app.layout=html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
    ),
    html.Div(id='output-data-upload'),
])

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')])
def parse_contents(contents):
    if not contents is None:#很重要要不页面会出错
        decoded = base64.b64decode(contents.split(",")[1])
        df=pd.read_table(io.StringIO(decoded.decode('utf-8')),sep="\t",header=0)
        return dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns]
            )


if __name__ == '__main__':
    app.run_server(debug=True)