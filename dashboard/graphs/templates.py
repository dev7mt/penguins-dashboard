from typing import List

import plotly.express as px
from dash import dcc
from data.external import penguins_df


def species_scatter(mass_range: List[float] = None) -> dcc.Graph:
    df = penguins_df()
    if mass_range is not None:
        df = df.loc[df.body_mass_g.between(*mass_range)]
    return dcc.Graph(
        id="species-scatter",
        figure=px.scatter(
            df,
            x="bill_length_mm",
            y="flipper_length_mm",
            color="species",
            hover_data=["species", "island", "body_mass_g"],
            title="Penguins!",
        ),
    )


def island_scatter(mass_range: List[float] = None) -> dcc.Graph:
    df = penguins_df()
    if mass_range is not None:
        df = df.loc[df.body_mass_g.between(*mass_range)]
    return dcc.Graph(
        id="island-scatter",
        figure=px.scatter(
            df,
            x="bill_length_mm",
            y="flipper_length_mm",
            color="island",
            hover_data=["species", "island", "body_mass_g"],
            title="Penguins!",
        ),
    )


def bar_chart_sex(mass_range: List[float] = None) -> dcc.Graph:
    df = penguins_df()
    if mass_range is not None:
        df = df.loc[df.body_mass_g.between(*mass_range)]
    return dcc.Graph(
        id="bar-chart-sex",
        figure=px.bar(
            df.groupby("sex")["body_mass_g"].mean().reset_index(),
            x="sex",
            y="body_mass_g",
            title="Penguins!",
        ),
    )
