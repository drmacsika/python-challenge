from src import app


def list_routes() -> dict:
    """List all available routes

    Returns: dict with all available routes
    """
    routes = [route.rule for route in app.url_map.iter_rules()]
    return {"routes": routes}
