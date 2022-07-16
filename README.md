# Dash Webb Compare

This project was inspired by [WebbCompare](https://github.com/JohnEdChristensen/WebbCompare) and all of the images
displayed are sourced from that project.  Thank you @JohnEdChristensen

There are __4 versions of the same app__ to demonstrate different features of Plotly Dash and community Dash components libraries.
Each of these amazing apps are made with ~100 _or fewer!_ lines of code.

After cloning this repo, run one of the 4 apps:

- `app_dbc.py` is made with dash-bootstrap-components
- `app_dmc.py` is made with dash-manitine-componets
- `app_pages.py` multi-page app using the new `pages` feature
- `app_pages_no_assets` multi-page app using `pages` with the images hosted remotely rather than in the `assets` folder.

Multi-page apps  

There are two apps that are made with using the new `pages` feature available in dash>=2.5.1.  Since the layout
is so simple neither one uses the `pages` folder, which is typical when more complex multi-page apps.
The advantage with using the `pages` feature that it automatically creates the meta tags for displaying
nicely formatted cards when the link is shared.  It also automatically updates the title for each page.
For more information on multi-page dash apps, see the [Plotly Dash docs](https://dash.plotly.com/urls)
