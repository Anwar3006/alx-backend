#!/usr/bin/env python3
"""

"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config():
    """
    Flask-Babel Configuration setup class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Retrieves langauge from user's request headers
    """
    locale = request.args.get('locale')
    if locale == 'fr':
        app.config['BABEL_DEFAULT_LOCALE'] = locale
        return app.config['BABEL_DEFAULT_LOCALE']
    else:
        return request.accept_languages.best_match(['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index():
    """
    Render html page from external source
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True
    )
