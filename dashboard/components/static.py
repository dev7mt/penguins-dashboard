import dash_bootstrap_components as dbc
from dash import html

penguin_logo = "https://cdn-icons-png.flaticon.com/512/627/627857.png"
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src=penguin_logo, height="50px")),
                    dbc.Col(dbc.NavbarBrand("Penguins dashboard", className="ms-2")),
                ],
                align="center",
                className="g-0",
            ),
        ]
    ),
    color="primary",
    dark=True,
)
