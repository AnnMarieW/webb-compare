# Dash Webb Compare

See the app live at https://dash-webb-compare.herokuapp.com/

__You can make an app like this in ~40 lines of code!__

There are _4 versions of the same app_ to demonstrate different features of [Plotly Dash](https://dash.plotly.com/) and
Dash community components libraries.  


### Dash app with dash-boostrap-components

![webb](https://user-images.githubusercontent.com/72614349/179326884-a9a01fef-6f64-4de0-a40f-b206f3a99ff8.gif)

### Dash app with dash-mantine-components

![web_dmc](https://user-images.githubusercontent.com/72614349/179326881-bab05723-0560-4bc7-9bbb-1ec5869cfac2.gif)


## Run one of the 4 apps:

- `app.py` is a minimal app made with [dash-mantine-componets](https://www.dash-mantine-components.com/) ~40 lines of code!
- `app_dbc.py` is made with [dash-bootstrap-components](https://dash-bootstrap-components.opensource.faculty.ai/) with the images hosted remotely rather than locally in the assets folder.
No need to clone this repo - simply copy, paste and run this app.
- `app_pages.py` multi-page app using the new `pages` feature
- `app_pages_no_assets` multi-page app using `pages` with the images hosted remotely rather than in the `assets` folder.

The before and after image slider is from the [dash-extensions library](https://www.dash-extensions.com/)


Multi-page apps  

There are two apps made with the new `pages` feature available in dash>=2.5.1.  Since the layout
is so simple neither one uses the `pages` folder, which is typical with multi-page apps.
The advantage of using the `pages` feature even with this simple app, is that it automatically creates the meta tags for displaying
nicely formatted cards when the link is shared.  It also automatically updates the title for each page.
For more information on multi-page dash apps, see the [Plotly Dash docs](https://dash.plotly.com/urls)



### Credits

This app was deployed using [dash-tools](https://github.com/andrew-hossack/dash-tools) DashTools is an open-source 
command line toolchain for Plotly Dash that makes creating and deploying dash projects to Heroku intuitive and easy. Thanks @andrew-hossack for providing such an awesome tool.  It truly makes deploying a Dash app a piece of cake.  :cake:

This project was inspired by [WebbCompare](https://github.com/JohnEdChristensen/WebbCompare) and all the before and after images
are sourced from that project.  Thanks @JohnEdChristensen

