from functools import reduce
from typing import List

import numpy as np
import pandas as pd
import seaborn as sns

_SEXES_REMAPPING = {"Male": "Male", "Female": "Female", "Unknown": float("nan")}


def penguins_df() -> pd.DataFrame:
    return sns.load_dataset("penguins")


def filter_penguins(
    df: pd.DataFrame, mass_range: List[float] = None, sexes_list: List[str] = None
) -> pd.DataFrame:
    if mass_range is not None:
        df = df.loc[df.body_mass_g.between(*mass_range)]

    if sexes_list is not None:
        sexes_list_remapped = [_SEXES_REMAPPING[sex] for sex in sexes_list]
        df = df.loc[df.sex.isin(sexes_list_remapped)]

    return df


def filter_penguins_by_selection(df, species_selection, island_selection):
    selections = []
    intersected_selection = None

    # extract selected points from each selection if possible and add as new list to selections
    for selection in [species_selection, island_selection]:
        if selection is not None:
            selected_points = [point["pointIndex"] for point in selection["points"]]
            selections.append(selected_points)

    # if only one selection was performed, use it without modification
    if len(selections) == 1:
        intersected_selection = selections[0]

    # if more than, get the intersection of those values
    elif len(selections) > 1:
        intersected_selection = reduce(np.intersect1d, selections).tolist()

    if intersected_selection is not None:
        df = df.loc[df.index.isin(intersected_selection)]
    return df
