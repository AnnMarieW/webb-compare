"""
This is an example of a multi-page app made with `pages` that does not use the pages folder or the `assets` folder.
The images  are hosted on github and the meta tags images are set using the `image_url` prop.

"""

import dash
from dash import Dash, html
from dash_extensions import BeforeAfter
import dash_bootstrap_components as dbc

deep_field = "https://user-images.githubusercontent.com/72614349/179115661-f8de6e4c-0dca-4628-ab67-3d525f5ac049.jpg"
stephans_quintet = "https://user-images.githubusercontent.com/72614349/179115662-32d348da-fa8b-481d-b4fc-9f7414f49de0.jpg"
webb_stephans_quintet = "https://user-images.githubusercontent.com/72614349/179115663-71578706-1ab5-45a5-b809-812c7c3028a7.jpg"
carina = "https://user-images.githubusercontent.com/72614349/179115665-9800b45c-e1dc-4aa7-8b34-885d48c61221.png"
southern_nebula = "https://user-images.githubusercontent.com/72614349/179115666-fdd204fc-e33d-4524-9ba5-a2611740f8a7.jpg"
webb_deep_field = "https://user-images.githubusercontent.com/72614349/179115668-2630e3e4-3a9f-4c88-9494-3412e606450a.jpg"
webb_southern_nebula = "https://user-images.githubusercontent.com/72614349/179115670-ef5bc561-d957-4e88-82dc-53ca53541b04.jpg"
webb_carina = "https://user-images.githubusercontent.com/72614349/179115673-15eaccb9-d17d-4667-84fb-e0a46fd444e8.jpg"
webb_cartwheel = "https://user-images.githubusercontent.com/72614349/184414634-fbd08745-94b9-4de6-8bce-c3607d9fd8db.png"
cartwheel = "https://user-images.githubusercontent.com/72614349/184414677-69e09ba2-9852-4dc7-9d3f-9024518dcd3c.png"
deep_field_gif = "https://user-images.githubusercontent.com/72614349/189536976-b7c386df-38bd-4e4e-be83-c1836d4d7abd.gif"

app = Dash(
    __name__,
    use_pages=True,
    pages_folder="",
    external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
)


header = html.Div(
    [
        html.H2("James Webb Space Telescope", className="display-3"),
        html.Div("First Images.  Compare before and after images of Hubble vs Webb."),
        dbc.Button(
            [html.I(className="bi bi-book me-2"), "webbtelescope.org"],
            color="light",
            className="text-white-50",
            href="https://webbtelescope.org/news/first-images/gallery",
        ),
        dbc.Button(
            [html.I(className="bi bi-github me-2"), "source code"],
            color="light",
            className="ms-2 text-white-50",
            href="https://github.com/AnnMarieW/webb-compare",
            title="Make an app like this with ~40 lines of Python using Plotly Dash",
        ),
    ],
)


def make_before_after(after, before):
    return html.Div(
        [
            html.Div(
                [html.Div("Hubble"), html.Div("Webb")],
                className="d-flex justify-content-between",
                style={"maxWidth": 1000},
            ),
            BeforeAfter(before={"src": before}, after={"src": after}),
        ],
        style={"marginTop": 50},
    )


def navbar():
    return dbc.Nav(
        [
            dbc.NavLink(
                html.Div(page["name"], className="ms-2"),
                href=page["path"],
                active="exact",
            )
            for page in dash.page_registry.values()
        ],
        pills=True,
        className="mt-5",
    )


descr = """James Webb Space Telescope First Images. Compare before and after images of Hubble vs Webb.  This app is made with Plotly Dash"""

dash.register_page(
    "Galaxy Cluster SMACS 0723",
    description=descr,
    image_url=deep_field_gif,
    layout=make_before_after(webb_deep_field, deep_field),
    path="/",
)
dash.register_page(
    "Cartwheel Galaxy",
    description=descr,
    image_url=webb_cartwheel,
    layout=make_before_after(webb_cartwheel, cartwheel),
)
dash.register_page(
    "stephans_quintet",
    description=descr,
    image_url=webb_stephans_quintet,
    layout=make_before_after(webb_stephans_quintet, stephans_quintet),
)
dash.register_page(
    "carina_nebula",
    description=descr,
    image_url=webb_carina,
    layout=make_before_after(webb_carina, carina),
)
dash.register_page(
    "southern_ring_nebula",
    description=descr,
    image_url=webb_carina,
    layout=make_before_after(webb_southern_nebula, southern_nebula),
)


app.layout = dbc.Container(
    [header, navbar(), dash.page_container], style={"maxWidth": 1000}
)

if __name__ == "__main__":
    app.run_server(debug=True)
