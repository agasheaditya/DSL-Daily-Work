import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import dash_table
import chart_studio.plotly as py
from chart_studio.plotly import iplot


df_g1 = pd.read_excel("X:\\DataScienceLab\\DSL-Daily-Work\\DSL-Daily-Work\\Data_for_plots.xlsx",sheet_name="Model 1_2018") #for 2017
df1_g1 = df_g1.drop(df_g1.index[0])
x_val_g1 = df1_g1['Forecasts:']
y1_actual_g1 = df1_g1['Actual']

y1_L95_g1 = df1_g1['Lo 95']
y1_H95_g1 = df1_g1['Hi 95']
y1_H80_g1 = df1_g1['Hi 80']
y1_L80_g1 = df1_g1['Lo 80']

trace_one_g1 = go.Scatter(
x=x_val_g1,
y=y1_actual_g1,
name="Actual",
line=dict(color='#3e8ebd'),
opacity=0.8
)

trace_two_g1 = go.Scatter(
x=x_val_g1,
y=y1_L95_g1,
name="Low 95",
line=dict(color='#fc513a'),
opacity=0.8
)

trace_three_g1 = go.Scatter(
x=x_val_g1,
y=y1_H95_g1,
name="High 95",
line=dict(color='#50d12c'),
opacity=0.8
)

trace_four_g1 = go.Scatter(
x=x_val_g1,
y=y1_L80_g1,
name="Low 80",
line=dict(color='#e352c3'),
opacity=0.8
)

trace_five_g1 = go.Scatter(
x=x_val_g1,
y=y1_H80_g1,
name="High 80",
line=dict(color='#b941e0'),
opacity=0.8
)
data = [trace_one_g1, trace_two_g1,trace_three_g1,trace_four_g1,trace_five_g1]
#layout = dict(title="Time Series Forecast Graph")
#fig = dict(data=data, layout=layout)