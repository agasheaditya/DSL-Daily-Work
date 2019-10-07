import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash()

tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Tab 1", tab_style={"margin-left": "auto"}),
                dbc.Tab(label="Tab 2", label_style={"color": "#00AEF9"}),
            ]
        ),
        html.Br(),

    ]
)

app1 = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app1.layout = html.Div([tabs])

if __name__=="__main__":
    app1.run_server(debug=True)