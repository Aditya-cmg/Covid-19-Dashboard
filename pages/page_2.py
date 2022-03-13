import dash
dash.register_page(__name__)

from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib

from combine import wrangle_data
from plotting_util import plot_config, get_map_plot, get_total_timeseries, get_country_timeseries,get_bar_plot

#get_data() #saving the live data to csv to avoid ban --> the app will connect to app everytime there is refresh- fix this
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
covid_df = pd.read_csv(DATA_PATH.joinpath("covid_19_clean_complete.csv"))  # GregorySmith Kaggle
pop_df = pd.read_csv(DATA_PATH.joinpath("macro_corona_data.csv"))

covid_df = wrangle_data(covid_df , pop_df)

def dropdown_options(col):
    return [{'label': name, 'value': name} for name in col]

def get_graph(class_name, **kwargs):
    return html.Div(
        className=class_name + ' plotz-container',
        children=[
            dcc.Graph(**kwargs),
            html.I(className='fa fa-expand'),
        ],
    )


control_panel = dbc.Card(
    [
        dbc.CardBody(
            [
                html.Div(
                    className='header',
                    children=[
                        dcc.Dropdown(
                            id='count_category',
                            className='radio-group',
                            options=dropdown_options(['Confirmed', 'Active', 'Recovered', 'Deaths']),
                            value='Confirmed',

                        ),
                        html.Span('|'),
                        dcc.Dropdown(
                            id='count_type',
                            className='radio-group',
                            options=[
                                {'label': 'Per Capita', 'value': 'per_capita'},
                                {'label': 'Actual', 'value': 'actual'}
                            ],
                            value='actual',
                        ),
                        dcc.Input(
                            id='country_input',
                            type='text',
                            debounce=True,
                        ),
                    ])
            ]
        ),
    ],
    color="light",
)

screen2 = html.Div(
    className='parent',
    children=[
        get_graph(
            class_name='div1',
            figure=get_bar_plot(covid_df),
            id='bar_graph',
            config=plot_config,
            clear_on_unhover=True,
        ),
        get_graph(
            class_name='div2',
            figure=get_country_timeseries(covid_df),
            id='country_graph',
            config=plot_config,
        ),
        get_graph(
            class_name='div3',
            figure=get_total_timeseries(covid_df),
            id='total_graph',
            config=plot_config,
        ),
    ])

layout = html.Div([
    dbc.Row([dbc.Col(control_panel)]) ,
    dbc.Row([dbc.Col(screen2)])
])

@callback(
    Output('bar_graph', 'figure'),
    [
        Input('count_type', 'value'),
        Input('count_category', 'value'),
    ])
def update_bar_plot(count_type, count_category):
    count_col = count_category if count_type == 'actual' else count_category + 'PerCapita'
    return get_bar_plot(covid_df, count_col)


@callback(
    Output('country_graph', 'figure'),
    [
        Input('count_type', 'value'),
        Input('count_category', 'value'),
    ])
def update_bar_plot(count_type, count_category):
    count_col = count_category if count_type == 'actual' else count_category + 'PerCapita'
    return get_country_timeseries(covid_df, count_col)


@callback(
    Output('total_graph', 'figure'),
    [
        Input('country_input', 'value'),
        Input('count_type', 'value')
    ])
def update_x_timeseries(country, count_type):
    df = covid_df[covid_df['Country'] == country] \
        if country \
        else covid_df
    return get_total_timeseries(
        df,
        country=country,
        per_capita=count_type == 'per_capita')

