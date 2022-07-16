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
article = "https://bigthink.com/starts-with-a-bang/before-and-after-james-webb/"
github="https://github.com/JohnEdChristensen/WebbCompare"


app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP])
app.title="Webb-before-after"

header = html.Div(
    [
        html.H2("James Webb Space Telescope", className="display-3"),
        html.P("First Images -- Before and After -- Hubble vs Webb"),
        dbc.Button("Article", color="light", outline=True, href=article),
        dbc.Button(
            [html.I(className="bi bi-github m-2"), "Images source"],
            color="light",  outline=True, className="mb-2", href=github
        ),
    ],
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


tabs = dbc.Tabs(
    [
        dbc.Tab(make_before_after( webb_deep_field, deep_field,), label="Galaxy Cluster SMACS 0723"),
        dbc.Tab(make_before_after( webb_stephans_quintet,stephans_quintet,),label="Stephans Quintet"),
        dbc.Tab(make_before_after(webb_carina, carina), label="Carina Nebula"),
        dbc.Tab(make_before_after(webb_southern_nebula, southern_nebula), label="Southern Ring Nebula"),
    ],
    className="mt-4",
)

app.layout = dbc.Container([header, tabs])

if __name__ == "__main__":
    app.run_server(debug=True)
