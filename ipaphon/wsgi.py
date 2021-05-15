import sys

from flask import Flask

from ipaphon.app import main
from ipaphon.config import read_config

MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB


def create_app():
    config = read_config()
    app = Flask(__name__)
    if "secret_key" in config:
        app.secret_key = config["secret_key"]
    else:
        print("Secret key missing in configuration file. Exiting.", file=sys.stderr)
        sys.exit(1)
    if "download_folder" in config:
        app.config["DOWNLOAD_FOLDER"] = config["download_folder"]
    else:
        print(
            "Download directory missing in configuration file. Exiting.",
            file=sys.stderr,
        )
        sys.exit(1)
    app.register_blueprint(main)
    if "content_limit" in config:
        app.config["MAX_CONTENT_LENGTH"] = config["content_limit"]
    app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH
    return app


def wsgi():
    app = create_app()
    return app


if __name__ == "ipaphon.wsgi":
    app = create_app()
