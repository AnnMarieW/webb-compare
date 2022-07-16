"""
This is an example of a multi-page app made with `pages` that does not use the pages folder.

"""

import dash
from dash import Dash, html
from dash_extensions import BeforeAfter
import dash_bootstrap_components as dbc


article = "https://bigthink.com/starts-with-a-bang/before-and-after-james-webb/"
github_web_compare = "https://github.com/JohnEdChristensen/WebbCompare"
github_amw = ""


app = Dash(
    __name__,
    use_pages=True,
    pages_folder="",
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
)


def make_before_after(before, after):
    return html.Div(
        [
            html.Div(
                [html.Div("Hubble"), html.Div("Webb")],
                className="d-flex justify-content-between",
                style={"width": 1000},
            ),
            BeforeAfter(before=before, after=after, height=800, width=1000),
        ],
        style={"marginTop": 50},
    )


descr = "James Webb Space Telescope First Images. Compare before and after images of Hubble vs Webb.  This app is made with Plotly Dash"

dash.register_page(
    "webb_deep_field",
    name="Galaxy Cluster SMACS 0723",
    description=descr,
    layout=make_before_after("/assets/webb_deep_field.jpg", "/assets/deep_field/jpg"),
    path="/",
)
dash.register_page(
    "webb_stephans_quintet",
    description=descr,
    layout=make_before_after(
        "/assets/webb_stephans_quintet.jpg", "/assets/stephans_quintet.jpg"
    ),
)
dash.register_page(
    "webb_carina",
    name="Carina Nebula",
    description=descr,
    layout=make_before_after("/assets/webb_carina.jpg", "/assets/carina.png"),
)
dash.register_page(
    "webb_southern_ring",
    name="Sounther Ring Nebula",
    description=descr,
    layout=make_before_after(
        "/assets/webb_southern_nebula.jpg", "/assets/southern_nebula.jpg"
    ),
)

header = html.Div(
    [
        html.H2("James Webb Space Telescope", className="display-3"),
        html.P(
            "First Images.  Compare before and after images of Hubble vs Webb."
        ),
        dbc.Button("Article", color="light", outline=True, href=article),
        dbc.Button(
            [html.I(className="bi bi-github m-2"), "Images Source"],
            color="light",
            outline=True,
            className="ms-2",
            href=github_web_compare,
        ),
        dbc.Button(
            [html.I(className="bi bi-github m-2"), "Source Code"],
            color="light",
            outline=True,
            className="ms-2",
            href=github_amw,
        ),
    ],
)


def navbar():
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            pills=True,
            className="mt-5",
        )
    )


app.layout = dbc.Container([header, navbar(), dash.page_container])

if __name__ == "__main__":
    app.run_server(debug=True)
