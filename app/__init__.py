from flask import Flask
from dash import Dash
from config import Config, blueprints, dash_apps
import importlib
import dash_bootstrap_components as dbc
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

# Set up the Flask application and add Dashboards


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():

        # Register blueprints listed in config.py
        for i in blueprints:
            module = importlib.import_module(f'app.blueprints.{i["name"]}')
            app.register_blueprint(module.bp)

        # Create Dash Apps listed in config.py
        for i in dash_apps:
            create_dashboard(server=app, folder_name=i['name'], multi_page=i['multi_page'])

    return app

# This function is used to dynamically create Dash Apps


def create_dashboard(server, folder_name, multi_page):
    url = folder_name.replace('dash_', '')
    if multi_page:
        dash_app = Dash(
            __name__,
            server=server,
            url_base_pathname=f'/{url}/',
            assets_folder=f'{folder_name}/assets',
            external_stylesheets=[dbc.themes.LUX,
                                  dbc.icons.FONT_AWESOME, dbc_css],
            use_pages=True,
            pages_folder=f'{folder_name}/pages'
        )
    else:
        dash_app = Dash(
            __name__,
            server=server,
            url_base_pathname=f'/{url}/',
            assets_folder=f'{folder_name}/assets',
            external_stylesheets=[dbc.themes.LUX,
                                  dbc.icons.FONT_AWESOME, dbc_css],
        )

    with dash_app.server.app_context():
        # Import and register Dash layouts and callbacks dynamically
        layouts_module = importlib.import_module(f'app.{folder_name}.layout')
        callbacks_module = importlib.import_module(
            f'app.{folder_name}.callbacks')
        dash_app.layout = layouts_module.layout
        callbacks_module.register_callbacks(dash_app)
