import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import dash_table
import plotly.plotly as py
from plotly.plotly import iplot

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_excel("Data_for_plots.xlsx")
df1 = df.drop(df.index[0])
x_val = df1['Forecasts:']
y1_val = df1['Actual']

y1_L95 = df1['Lo 95']
y1_H95 = df1['Hi 95']

trace_one = go.Scatter(
    x=x_val,
    y=y1_val,
    name="Actual",
    line=dict(color='#17BECF'),
    opacity=0.8
)
trace_two = go.Scatter(
    x=x_val,
    y=y1_L95,
    name="Low 95",
    line=dict(color='#7F7F7F'),
    opacity=0.8
)
trace_three = go.Scatter(
    x=x_val,
    y=y1_H95,
    name="High 95",
    line=dict(color='#5F5F5F'),
    opacity=0.8
)
data = [trace_one, trace_two,trace_three]
layout = dict(title="Time Series Forecast Graph")
fig = dict(data=data, layout=layout)
#iplot(fig,filename="Forecast Trace")


tab1 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Container(
                        html.Ul(["Part1", html.Br(),
                                 html.A("subpart1", href="demo.py"), html.Br(),
                                 html.A("subpart2", href="demo.py"), html.Br(),
                                 html.A("subpart3", href="##"), html.Br(),
                                 html.Ul(["Part2", html.Br(),
                                          html.A("subpart4", href="##", ), html.Br(),
                                          html.A("subpart5", href="##"), html.Br(),
                                          html.A("subpart6", href="##"), html.Br(),

                                          ]),
                                 ]),
                        className="mt-4",
                    )
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(
                            # figure={"data": [{"x": x1_val, "y": y1_val}]}
                            figure=fig

                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

table_header = [
    html.Thead(html.Tr([html.Th("Data"), html.Th("Y")]))
]

# row1 = html.Tr([html.Td("Data"), html.Td("Y")])
row2 = html.Tr([html.Td(), html.Td("1")])
row3 = html.Tr([html.Td("2"), html.Td("4")])
row4 = html.Tr([html.Td("3"), html.Td("3")])
row5 = html.Tr([html.Td("4"), html.Td("9")])
row6 = html.Tr([html.Td("5"), html.Td("6")])
row7 = html.Tr([html.Td("6"), html.Td("2")])

table_body = [html.Tbody([row2, row3, row4, row5, row6, row7])]
table = dbc.Table(table_header + table_body, bordered=True)

tab2 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Container(
                        html.Ul(["Part1", html.Br(),
                                 html.A("subpart1", href="demo.py"), html.Br(),
                                 html.A("subpart2", href="demo.py"), html.Br(),
                                 html.A("subpart3", href="##"), html.Br(),
                                 html.Ul(["Part2", html.Br(),
                                          html.A("subpart4", href="##", ), html.Br(),
                                          html.A("subpart5", href="##"), html.Br(),
                                          html.A("subpart6", href="##"), html.Br(),

                                          ]),
                                 ]),
                        className="mt-4",
                    )
                ),
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
                ),
            ]
        )
    ],
    className="mt-4",

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

if __name__ == "__main__":
    app1.run_server(debug=True)
