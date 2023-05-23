#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config():
    """
    Flask-Babel Configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """
    Retrieve locale from the request header sent by the user
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Render html page from external source
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(
        host='localhost',
        port='5000',
        debug=True
    )
