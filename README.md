# Dash Webb Compare

See the app live at https://dash-webb-compare.herokuapp.com/

https://dash-webb-compare.herokuapp.com/

This project was inspired by [WebbCompare](https://github.com/JohnEdChristensen/WebbCompare) and all the images
displayed are sourced from that project.  Thank you @JohnEdChristensen

There are __4 versions of the same app__ to demonstrate different features of Plotly Dash and community Dash components libraries.
Each of these apps are made with ~100 _or fewer!_ lines of code.

After cloning this repo, run one of the 4 apps:

- `app_dbc.py` is made with [dash-bootstrap-components](https://dash-bootstrap-components.opensource.faculty.ai/)
- `app_dmc.py` is made with [dash-mantine-componets](https://www.dash-mantine-components.com/)
- `app_pages.py` multi-page app using the new `pages` feature
- `app_pages_no_assets` multi-page app using `pages` with the images hosted remotely rather than in the `assets` folder.

The before and after image slider is from the [dash-extensions library](https://www.dash-extensions.com/)


Multi-page apps  

There are two apps made with the new `pages` feature available in dash>=2.5.1.  Since the layout
is so simple neither one uses the `pages` folder, which is typical with multi-page apps.
The advantage of using the `pages` feature even with this simple app, is that it automatically creates the meta tags for displaying
nicely formatted cards when the link is shared.  It also automatically updates the title for each page.
For more information on multi-page dash apps, see the [Plotly Dash docs](https://dash.plotly.com/urls)


### Dash app with dash-boostrap-components

![webb](https://user-images.githubusercontent.com/72614349/179326884-a9a01fef-6f64-4de0-a40f-b206f3a99ff8.gif)

### Dash app with dash-mantine-components

![web_dmc](https://user-images.githubusercontent.com/72614349/179326881-bab05723-0560-4bc7-9bbb-1ec5869cfac2.gif)


### This app was deployed using [dash-tools](https://github.com/andrew-hossack/dash-tools)  

DashTools is an open-source command line toolchain for Plotly Dash that makes creating and deploying dash projects to Heroku intuitive and easy.  

Thanks @andrew-hossack for providing such an awesome tool.  It truly makes deploying an app a piece of cake.  :cake:


