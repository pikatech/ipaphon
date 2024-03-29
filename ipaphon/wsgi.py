"""
The starting point for both 'flask run'
and any WSGI server that will run the app.
"""
import sys

from flask import Flask

from ipaphon.app.ipaphon import main
from ipaphon.config import read_config

MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB


def create_app() -> Flask:
    """
    Create an instance of the Flask app.
    The configuration settings get passed to the Flask app
    and all of the routes are connected via the blueprint.

    Returns
    -------
    Flask
        An instance of a Flask app
    """
    config = read_config()
    wsgi_app = Flask(__name__)
    if "secret_key" in config:
        wsgi_app.secret_key = config["secret_key"]
    else:
        print("Secret key missing in configuration file. Exiting.", file=sys.stderr)
        sys.exit(1)
    wsgi_app.register_blueprint(main)
    if "content_limit" in config:
        wsgi_app.config["MAX_CONTENT_LENGTH"] = config["content_limit"]
    wsgi_app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH
    return wsgi_app


def wsgi() -> Flask:
    """WSGI servers like Waitress can access the app via this function."""
    app = create_app()
    return app


if __name__ == "ipaphon.wsgi":
    app = create_app()
