import dash_core_components as dcc
import dash_html_components as html
import dash

app=dash.Dash(__name__)
app.layout=html.Div([
    dcc.Markdown('''
1.  *在从fastq格式开始分析TSO500数据时，SampleSheet.csv文件中需要将Workflow这一行标注为：From GenerateFASTQ,默认为GenerateFASTQ*
2.  
''')
]
)


if __name__=="__main__":
    app.run_server(debug=True)
