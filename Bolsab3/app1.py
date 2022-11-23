from re import template
import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd


app =dash.Dash(__name__)

colors= (
    'background' :'#111111',
    'text' : '#7FDBFF'
)

df = pd.read_csv('')