import pandas as pd
import seaborn as sns


def penguins_df() -> pd.DataFrame:
    return sns.load_dataset("penguins")
