from dash import dcc
from data.external import penguins_df


# function that creates a rangeslider from our dataset
def penguins_mass_slider() -> dcc.RangeSlider:
    df = penguins_df()  # load dataset temporarily, calculate min, max, mean, std
    min_ = int(df.body_mass_g.min())
    max_ = int(df.body_mass_g.max())
    mean_ = int(df.body_mass_g.mean())
    std_ = int(df.body_mass_g.std())

    # generate a range from min to max with step 200; alt: np.arange(min, max, step)
    body_mass_steps = range(min_, max_, 200)

    # dictionary comprehension
    # {a: a * 10 for a in [1, 2, 3]}
    # {new_key: new_value for key, val in another_dict.items()}
    # {v: modified_v for v in list}
    marks = {}
    for i, step in enumerate(body_mass_steps):
        if i % 2 == 0:
            marks[step] = f"{step}g"
        else:
            marks[step] = ""

    # marks = {0: "poczatek", 100: "koniec"}
    # add true min and max to marks
    marks[min_] = f"{min_}g"
    marks[max_] = f"{max_}g"

    # create slider, from min to max, step=1, with default values of mean 士 std. dev.
    slider = dcc.RangeSlider(
        min=min_,
        max=max_,
        step=None,
        value=[mean_ - std_, mean_ + std_],
        marks=marks,
        id="penguins-mass-slider",
    )
    return slider


def penguins_sex_checklist() -> dcc.Checklist:
    checklist = dcc.Checklist(
        options=["Male", "Female", "Unknown"],
        value=["Male", "Female"],
        inline=True,
        id="penguins-sex-checklist",
    )
    return checklist
