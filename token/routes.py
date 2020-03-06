from views import verify_token


def setup_routes(app):
    app.router.add_post('/public/v1/verify/', verify_token)
