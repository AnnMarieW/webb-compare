from dash import Dash, html
from dash_extensions import BeforeAfter
import dash_mantine_components as dmc

app = Dash(__name__)

header = html.Div(
    [
        dmc.Title("James Webb Space Telescope", order=1),
        dmc.Text("First Images -- Before and After -- Hubble vs Webb"),
        dmc.Space(h="md"),
    ],
)


def make_before_after(before, after):
    return html.Div(
        [
            dmc.Space(h=40),
            dmc.Group(
                [dmc.Text("Hubble"), dmc.Text("Webb")],
                position="apart",
                style={"width": 1000},
            ),
            BeforeAfter(before=before, after=after, height=800, width=1000),
        ],
    )


tabs = dmc.Tabs(
    [
        dmc.Tab(make_before_after("/assets/webb_deep_field.jpg", "/assets/deep_field.jpg"), label="Galaxy Cluster SMACS 0723"),
        dmc.Tab(make_before_after("/assets/webb_stephans_quintet.jpg", "/assets/stephans_quintet.jpg"), label="Stephans Quintet"),
        dmc.Tab(make_before_after("assets/webb_carina.jpg", "/assets/carina.png"), label="Carina Nebula"),
        dmc.Tab(make_before_after("assets/webb_southern_nebula.jpg", "assets/southern_nebula.jpg"), label="Southern Ring Nebula"),
    ],
)

app.layout = dmc.MantineProvider(
    dmc.Container([header, tabs]), theme={"colorScheme": "dark"}, withGlobalStyles=True
)

if __name__ == "__main__":
    app.run()
