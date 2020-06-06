# Flask-PyNgrok
Tunneling local web server for development using [PyNgrok](https://pypi.org/project/pyngrok/).

Installation
------------

Flask-PyNgrok is available on [PyPI](https://pypi.org/project/Flask-PyNgrok/) and can be installed using pip.

    pip install Flask-PyNgrok


Basic Usage
-----------

Flask setting required `FLASK_ENV=development`:
    from Flask-PyNgrok import PyNgrok
    pyngrok = PyNgrok()

    def create_app(config):
        app = Flask(__name__)
        app.config.from_object(config)
        pyngrok.init_app(app)

    app = create_app(dev_config)


License
-------

Flask-PyNgrok is distributed under MIT license, see LICENSE for more details.

