from dash import Dash


def create_dashboard(server):
    dash_app = Dash(
        __name__,
        server=server,
        url_base_pathname='/dashboard/',
        assets_folder='assets',
        external_stylesheets=['/static/bootstrap.min.css']
    )

    with dash_app.server.app_context():
        from .layout import layout
        from .callbacks import register_callbacks
        dash_app.layout = layout
        register_callbacks(dash_app)

    return dash_app
