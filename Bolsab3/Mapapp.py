from re import template
from dash import dcc, html, Dash
import yfinance as yf
import plotly.express as px
import pandas as pd
from selenium import webdriver
import datetime
import webbrowser
import time

app = Dash(__name__)
colors= {
    'background' :'#111111',
    'text' : '#7FDBFF'
}
yf.pdr_override()
start = datetime.datetime(2009, 1, 1)
end = datetime.datetime(2022, 11, 1)

options = webdriver.ChromeOptions()
prefs ={"download.default_directory" : "Users/juliocarvalho/Downloads/"}

options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options)
driver.get ("https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br")

btn_download = driver.find_element("link text",'Download')
btn_download.click()

driver.close()

df = pd.read_csv("/Users/juliocarvalho/Desktop/PosMapa/Bolsab3/IBOVDia_10-11-22.csv",error_bad_lines=False, sep=';', skiprows=1)

df.head()
df.info()
df.index[:-2]

ativos = list(df.index[:-2])
ativos = map(lambda a: f"{a}.SA", ativos)
ativos_sa =" ".join(list(ativos))

ativos_sa
yf.pdr_override()
cotacoes_ativos = yf.download(tickers=ativos_sa,period='1Y')
cotacoes_ativos['Adj Close'].info()
cotacoes_ativos.head()
cotacoes_ativos_fechamentos =cotacoes_ativos['Adj Close']


fig =px.bar(df, x='Tipo', y='Tipo',color='Codigo',barmode="group")

app.layout =html.Div(children=[
    html.H1(children='Mapa Bolsab3'),
    html.Div(children='''
        Dash: A web application that'''),
    dcc.Graph(
        id='exemplep-graph',
        figure=fig
        )
])

if __name__ == "__main__":
    app.run_server()