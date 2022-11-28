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

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/9166432/raw/0d5410f1f8da88670adc86080e7154009ebf4906/indicator%2520gapminder%2520gdp_per_capita_ppp%2520-%2520Data.csv')

fig_scater = px.scater(df, x="gpd per capita", y="Life expectation".
             size= popu       )
             