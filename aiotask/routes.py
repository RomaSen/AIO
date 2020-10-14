from .views import summator


def setup_routes(app):
    app.router.add_route('GET', '/', summator.SummatorView)
    # app.router.add_route('POST', '/', summator.SummatorView)
