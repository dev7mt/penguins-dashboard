from typing import List, Tuple

import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, dash_table, dcc, html

from components.filtering import penguins_mass_slider, penguins_sex_checklist
from components.static import navbar

# import from our packages with components and graphs
from data.external import filter_penguins, penguins_df
from graphs.templates import bar_chart_sex, island_scatter, species_scatter

# creating appliaction
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# layout - how the application looks
app.layout = html.Div(
    [
        navbar,
        html.Br(),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(html.Span("Select penguins body mass:"), width=2),
                        dbc.Col(penguins_mass_slider(), width=6),
                        dbc.Col(html.Span("Select penguins sex:"), width=2),
                        dbc.Col(penguins_sex_checklist(), width=2),
                    ]
                ),
                dbc.Row(
                    [  # we are changing the `Col` component, altering it's children, instead of just a figure
                        dbc.Col(
                            id="species-scatter-col",
                            children=species_scatter(),
                            width=5,
                        ),
                        dbc.Col(
                            id="island-scatter-col", children=island_scatter(), width=4
                        ),
                        dbc.Col(
                            id="bar-chart-sex-col", children=bar_chart_sex(), width=3
                        ),
                    ]
                ),
                dbc.Row(
                    dbc.Col(
                        dash_table.DataTable(
                            data=penguins_df().to_dict("records"),
                            columns=[
                                {"name": i, "id": i} for i in penguins_df().columns
                            ],
                            page_action="native",
                            page_current=0,
                            page_size=10,
                            id="penguins-table",
                        )
                    )
                ),
            ]
        ),
        html.Br(),
    ],
)

# callback modifing scatters and bar charts
@app.callback(
    Output("species-scatter-col", "children"),
    Output("island-scatter-col", "children"),
    Output("bar-chart-sex-col", "children"),
    Input("penguins-mass-slider", "value"),  # <- min,max values from slider
    Input("penguins-sex-checklist", "value"),  # <- values from checklist
)
def adjust_main_graphs(
    mass_range: List[float], sexes_list: List[str]
) -> Tuple[dcc.Graph, dcc.Graph, dcc.Graph]:
    return (
        species_scatter(mass_range, sexes_list),
        island_scatter(mass_range, sexes_list),
        bar_chart_sex(mass_range, sexes_list),
    )


@app.callback(
    Output("penguins-number-field", "children"),
    Output("penguins-table", "data"),
    Input("penguins-mass-slider", "value"),
    Input("penguins-sex-checklist", "value"),
)
def adjust_textual_data(mass_range: List[float], sexes_list: List[str]) -> str:
    df = penguins_df()
    df = filter_penguins(df, mass_range, sexes_list)
    penguins_count = len(df)
    penguins_count_text = f"Number of penguins: {penguins_count}"
    return penguins_count_text, df.to_dict("records")


# safety - only when running `python path-to-this-file.py` this code will run
if __name__ == "__main__":
    app.run_server(
        port=8062,
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_max_retry=5,
        dev_tools_hot_reload_interval=5,
    )
