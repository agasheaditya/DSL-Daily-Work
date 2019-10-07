import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

sidenav = dbc.Col(
                dbc.Container(
                             html.Ul(["Part1",html.Br(),
                             html.A("subpart1",href="##",),html.Br(),
                             html.A("subpart2",href="##"),html.Br(),
                             html.A("subpart3",href="##"),html.Br(),
                             html.Ul(["Part2",html.Br(),
                             html.A("subpart4",href="##",),html.Br(),
                             html.A("subpart5",href="##"),html.Br(),
                             html.A("subpart6",href="##"),html.Br(),

            ]),
            ]),
                    className="mt-4",
)
)
app1 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app1.layout = html.Div([sidenav])

if __name__ == "__main__":
    app1.run_server(debug=True)