import sys

from pyngrok import ngrok


class PyNgrok(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.env = app.config["FLASK_ENV"]
        self.connect(app)

    def connect(self, app):
        if self.env == "development":
            port = (
                sys.argv[sys.argv.index("--port") + 1]
                if "--port" in sys.argv
                else 5000  # noqa
            )
            public_url = ngrok.connect(port).public_url
            print(
                ' * ngrok tunnel "{}" -> "http://127.0.0.1:{}/"'.format(
                    public_url, port
                )
            )
            app.config["BASE_URL"] = public_url
