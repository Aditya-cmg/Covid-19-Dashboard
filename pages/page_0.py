import dash
dash.register_page(__name__, path="/")

import dash_bootstrap_components as dbc
import plotly.express as px
import pathlib

from combine import wrangle_data
from plotting_util import plot_config, get_map_plot

from dash import Dash, dcc, html, Input, Output, callback,State
import pandas as pd

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
covid_df = pd.read_csv(DATA_PATH.joinpath("covid_19_clean_complete.csv"))  # GregorySmith Kaggle
pop_df = pd.read_csv(DATA_PATH.joinpath("macro_corona_data.csv"))

covid_df = wrangle_data(covid_df , pop_df)

#A helper function
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


# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

about_app = html.Div(
    children=[
        html.Ul([
            html.Li(
                html.A('COVID Dataset',
                       href='https://www.kaggle.com/imdevskp/corona-virus-report')),
            html.Li(
                html.A('Code Link', href='https://github.com/nite/covid-19')),
        ]),
        html.P('''
       This interactive data visualisation webapp illustrates what is possible using the Open Source Plotly Dash library and very little code.
       Note that this is app development: not intended for 'production',and more for prototyping and educational purposes. 
       Think of it as a completely free Tableau, with the power of python for data science & machine learning. 
        '''),
        html.P('''
        The source code is in the GitHub.
        The dashboard is optimised for desktop, laptop and tablet/mobile average sized screens - it may or may not work on small sized mobile screen.
        '''),
        html.P('''
        All plots are interactive - hit play on the map, hover over bubbles, lines & points for dynamic annotations.
        You can zoom using your mouse (drag to select area to zoom into), mouse wheel or trackpad, and double click to zoom out & reset . 
        Click lines in legends to hide & show, or double-click to show only one line. 
        Be sure to use zoom on the map because the bubbles overlap & become a lot clearer on zooming.
        '''),
        html.P('''
        To switch between Confirmed, Active & Recorded, and Per Capita/Actual,
         use the dropdown menus in the control panel.
        '''),
        html.P('''
        The code is intended as a showcase of what is possible 
        in very few lines of python Plotly Dash code. 
        For example, take a look at plot.py in the github repo for the single line of 
        Plotly Express code to generate the scatter_mapbox with animating timeline.  
        '''),
        html.P('''
        Kaggle Data which is generated & cleaned from the CSSEGISandData/COVID-19 
        dataset (also on GitHub) is used
        '''),
        html.P('''
        Per Capita numbers are number / Population * 100,000 
        '''),
        html.P('''
        Stay Tuned and Enjoy!!
        '''),
    ]
)

modal = html.Div(
    [
        dbc.Button("About ", id="open_modal"),

        dbc.Modal([
            dbc.ModalHeader("All About the Project"),
            dbc.ModalBody(
                children=[
                    about_app,
                ]
            ),
            dbc.ModalFooter(
                dbc.Button("Close", id="close", className="ml-auto")
            ),

        ],
            id="modal",
            is_open=False,    # True, False
            size="xl",        # "sm", "lg", "xl"
            backdrop=True,    # True, False or Static for modal to not be closed by clicking on backdrop
            scrollable=True,  # False or True if modal has a lot of text
            centered=True,    # True, False
            fade=True         # True, False
        ),
    ]
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
                            #labelStyle={'display': 'inline-block'}
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
                            #labelStyle={'display': 'inline-block'}
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

screen1 = html.Div(
    className='parent',
    children=[
        get_graph(
            class_name='div1',
            figure=get_map_plot(covid_df),
            id='map_graph'
        )
    ])


layout = html.Div([
    html.Div(
        className='header',
        children=[
            html.Div(
                className='title',
                children=[
                    html.H4('COVID-19 Live Tracker | John Hopkins Kaggle Data'),
                ]
            ),
            html.Div(
                className='header',
                children=[
                    modal,
                    control_panel
                ])
        ]),
    screen1
    ])

#for creating modal popup
@callback(
    Output('modal', 'is_open'),
    [Input('open_modal', 'n_clicks'), Input('close', 'n_clicks')],
    [State('modal', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output('map_graph', 'figure'),
    [
        Input('count_type', 'value'),
        Input('count_category', 'value'),
    ])
def update_map_plot(count_type, count_category):
    count_col = count_category if count_type == 'actual' else count_category + 'PerCapita'
    return get_map_plot(covid_df, count_col)

