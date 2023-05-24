#!/usr/bin/env python3
"""
Parametrize templates
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Retrieves langauge from user's request headers
    """
    return request.accept_languages.best_match(['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Render html page from external source
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(
        'localhost',
        5000,
        True
    )
