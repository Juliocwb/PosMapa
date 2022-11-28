from re import template
import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd


app =dash.Dash(__name__)

colors= {
    'background' :'#111111',
    'text' : '#7FDBFF'
}

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/9166432/raw/0d5410f1f8da88670adc86080e7154009ebf4906/indicator%2520gapminder%2520gdp_per_capita_ppp%2520-%2520Data.csv')

fig_scatter = px.scatter(df, x="gpd per capita", y="Life expectation",
             size= "population", color= "continenet", hover_name="country",
             template='plotly_dark')

fig_bar = px.bar(df, x="country", y="life expectancy", color=" gpd per capita", barmode="group")

fig_scatter.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)

fig_bar.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)

def header():
    return html.Div(
        style={
            'backgroundColor': colors['background'],
            'padding': 10,
            'flex': 1
        },
        children=[
            html.H1(
                children='Analise de densidade Populacional',
                style={
                    'textAling': 'center',
                    'color': colors['text']
                }
            )
        ]
    )
def body():
    return html.Div(
        style={'display': 'felx','felx.direction': 'row'},
        children=[
            html.Div(
                style={
                    'backgroundColor': colors['background'],
                    'padding': 10,
                    'flex': 1
                },
                children=[
                    dcc.Graph(
                        id='example-graph-2',
                        figure=fig_scater
                    ),
                ]
            ),
            html.Div(
                style={
                    'backgroundColor': colors['background'],
                    'padding': 10,
                    'flex': 1
                },
                children=[
                    dcc.Graph(
                        id='example-graph-1',
                        figure=fig_bar
                    ),
                ]
            )

    ])
def footer():
    return html.Div(
            style={
                'backgroundColor': colors['background'],
                'padding': 10,
                'flex': 1
            },
            children=[
                dash_table.DataTable(
                    id='talbe',
                    columns=[{"name": i, "id": i} for i in df.column],
                    data=df.to_dict('records')
                )
            ]
    )
app.layout = html.Div([
    header(),
    body(),
    footer()
])

if __name__ == '__main__':
    app.run_server(debug=True)