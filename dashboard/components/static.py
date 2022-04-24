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
            html.Span(
                children=[], id="penguins-number-field", style={"color": "white"}
            ),
            dbc.Button(
                "Preset",
                color="warning",
                className="me-1",
                id="preset-button",
            ),
            dbc.Button(
                "Reload",
                color="warning",
                className="me-1",
                href="/",
                external_link=True,
            ),
        ]
    ),
    color="primary",
    dark=True,
)
