from typing import List, Tuple

import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, dcc, html

from components.filtering import penguins_mass_slider

# import from our packages with components and graphs
from components.static import navbar
from graphs.templates import bar_chart_sex, island_scatter, species_scatter

# creating appliaction
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# layout - how the application looks
app.layout = html.Div(
    [
        navbar,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(html.B("Select penguins body mass:"), width=3),
                dbc.Col(penguins_mass_slider(), width=9),
            ]
        ),
        dbc.Row(
            [  # we are changing the `Col` component, altering it's children, instead of just a figure
                dbc.Col(id="species-scatter-col", children=species_scatter(), width=5),
                dbc.Col(id="island-scatter-col", children=island_scatter(), width=4),
                dbc.Col(id="bar-chart-sex-col", children=bar_chart_sex(), width=3),
            ]
        ),
    ],
)

# comment fot git-related purposes


def fn(a, b):
    return a + b


# callback modifing scatters and bar charts
@app.callback(
    Output("species-scatter-col", "children"),
    Output("island-scatter-col", "children"),
    Output("bar-chart-sex-col", "children"),
    Input("penguins-mass-slider", "value"),
)
def adjust_mass_range(
    mass_range: List[float],
) -> Tuple[dcc.Graph, dcc.Graph, dcc.Graph]:
    return (
        species_scatter(mass_range),
        island_scatter(mass_range),
        bar_chart_sex(mass_range),
    )


# safety - only when running `python path-to-this-file.py` this code will run
if __name__ == "__main__":
    app.run_server(
        port=8062,
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_max_retry=5,
        dev_tools_hot_reload_interval=5,
    )
