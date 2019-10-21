import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import dash_table
import chart_studio.plotly as py
from chart_studio.plotly import iplot
from dash.dependencies import Input,Output
import graph1 as g1
import graph2 as g2

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#df = pd.read_excel("https://github.com/skad00sh/temp-dataset/blob/master/Data_for_plots.xlsx",sheet_name="Model 1_2018") # for 2018
df = pd.read_excel("X:\\DataScienceLab\\DSL-Daily-Work\\DSL-Daily-Work\\Data_for_plots.xlsx",sheet_name="Model 1_2017") #for 2017
df1 = df.drop(df.index[0])
x_val = df1['Forecasts:']
y1_actual = df1['Actual']

y1_L95 = df1['Lo 95']
y1_H95 = df1['Hi 95']
y1_H80 = df1['Hi 80']
y1_L80 = df1['Lo 80']

trace_one = go.Scatter(
    x=x_val,
    y=y1_actual,
    name="Actual",
    line=dict(color='#3e8ebd'),
    opacity=0.8
)
trace_two = go.Scatter(
    x=x_val,
    y=y1_L95,
    name="Low 95",
    line=dict(color='#fc513a'),
    opacity=0.8
)
trace_three = go.Scatter(
    x=x_val,
    y=y1_H95,
    name="High 95",
    line=dict(color='#50d12c'),
    opacity=0.8
)
trace_four = go.Scatter(
    x=x_val,
    y=y1_L80,
    name="Low 80",
    line=dict(color='#e352c3'),
    opacity=0.8
)
trace_five = go.Scatter(
    x=x_val,
    y=y1_H80,
    name="High 80",
    line=dict(color='#b941e0'),
    opacity=0.8
)
data = [trace_one, trace_two,trace_three,trace_four,trace_five]
layout = dict(title="Time Series Forecast Graph")
fig = dict(data=data, layout=layout)
#iplot(fig,filename="Forecast Trace")

tab1 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Container(
                        html.Ul(["2017", html.Br(),
                                 dbc.FormGroup([

                                dbc.RadioItems(id='radio_1',
                                    options=[
                                        {"label": "Option 1", "value": 'opt1'},
                                        {"label": "Option 2", "value": 'opt2'},
                                        {"label": "Option 3", "value": 'opt3'},
                                    ],
                                    

                                ),

                                 html.Ul(["2018", html.Br(),

                                                  dbc.RadioItems( id= 'radio_2',
                                                  options=[
                                                      {"label": "Actual", "value": 'opt4'},
                                                      {"label": "Low 95 and High 95", "value": 'opt5'},
                                                      {"label": "All Values", "value": 'opt6'},
                                                  ],
                                                  value= 'default',

                                              ),


                                    ]),
                                 ]),
                                 ]),id="radioitems-input",
                        className="col-sm",
                    )
                ,width={"size": 3, "offset": 0}),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(id="graph-with-radio",
                            # figure={"data": [{"x": x1_val, "y": y1_val}]}
                            #figure=fig,


                       ),
                    ]
                ,width={"size": 6, "offset": 1}),
            ]
        )
    ],
    className="col-sm",
)






tab2 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Container(
                        className="col-sm",
                    )
                ,width={"size": 3, "offset": 0}),
                dbc.Col(
                    [
                        html.H2("Table"),
                        dash_table.DataTable(
                            #table_header + table_body,
                            #bordered=True,
                            #dark=True,
                            #hover=True,
                            #responsive=True,
                            #striped=True,
                            id='table',
                            columns=[{"name": i, "id": i} for i in df.columns],
                            data=df1.to_dict('records'),
                        )
                    ]
                ,width={"size": 6, "offset": 1}),
            ]
        )
    ],
    className="col-sm",
)

tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(tab1, label="Forecast", tab_style={"margin-left": "45%"}),
                dbc.Tab(tab2, label="Data", label_style={"color": "#00AEF9"}),
            ]
        ),
        html.Br(),
    ]
)

PLOTLY_LOGO = "https://media.glassdoor.com/sqll/1992780/datasciencelab-squarelogo-1531383653363.png"
navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("DataScienceLab", className="ml-2")),
                    dbc.Col(
                        dbc.DropdownMenu(className="ml-5", children=[dbc.DropdownMenuItem("More pages", header=True),
                                                                     dbc.DropdownMenuItem("Page 2", href="demo.py"),
                                                                     dbc.DropdownMenuItem("Page 3", href="#"),
                                                                     dbc.DropdownMenuItem("Page 4", href="#"), ],
                                         label="More Pages", )
                    )
                ],
                align="right",
                no_gutters=True,
            ),

        ),
    ],
    color="dark",
    dark=True,
)

app1 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app1.layout = html.Div([navbar, tabs])

@app1.callback(
    Output('graph-with-radio', 'figure'),
    [Input('radio_2', 'value')]
)
def update_graph(value):
    data_dict = {
       'default' : data,
       # 'opt1': [g2.trace_one],
       # 'opt2': [g2.trace_two, g2.trace_three],
        #'opt3': [g2.trace_one, g2.trace_two1, g2.trace_three, g1.trace_four, g2.trace_five ],
        'opt4': [g1.trace_one_g1],
        'opt5': [g1.trace_two_g1, g1.trace_three_g1],
        'opt6': [g1.trace_one_g1, g1.trace_two_g1, g1.trace_three_g1, g1.trace_four_g1, g1.trace_five_g1 ]
    }
    title_dict = {
       'default': 'All values without clicking all values',
       #'opt1': 'Actual Values',
       #'opt2': 'Low 95 and High 95',
       #'opt3': 'All Values Together',
        'opt4': 'Actual Values',
        'opt5': 'Low 95 and High 95',
        'opt6': 'All Values Together'

    }
    return {
        'data' : data_dict[value],
        'layout': {
            'title' : title_dict[value]
        }
    }

'''@app1.callback(
    Output('graph-with-radio', 'figure'),
    [Input('radio_1', 'value')]
)
def update_graph(value):
    data_dict = {
        '' : data,
        'opt1': [g2.trace_one],
        'opt2': [g2.trace_two, g2.trace_three],
        'opt3': [g2.trace_one, g2.trace_two1, g2.trace_three1, g1.trace_four, g2.trace_five ]
    }
    title_dict = {
        '': 'All values without clicking all values',
        'opt1': 'Actual Values',
        'opt2': 'Low 95 and High 95',
        'opt3': 'All Values Together'

    }
    return {
        'data' : data_dict[value],
        'layout': {
            'title' : title_dict[value]
        }
    }'''





if __name__ == "__main__":
    app1.run_server(debug=True)
