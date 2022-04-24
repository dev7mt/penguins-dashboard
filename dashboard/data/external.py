from typing import List

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
