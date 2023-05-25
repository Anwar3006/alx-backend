#!/usr/bin/env python3
"""
Mock logging in
Imitating a user login system
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel


class Config():
    """
    Flask-Babel Configuration Setup class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Retrieve language from user's request header
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match('LANGAUGE')


def get_user():
    """
    Retrieves ID from URL passed as a query string
    Returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed
    """
    user_ID = request.args.get('login_as')
    if user_ID:
        return users.get(int(user_ID))
    return None


@app.before_request
def before_request():
    """
    Should use get_user to find a user if any,
    and set it as a global on flask.g.user.
    """
    obtain_user = get_user()
    g.user = obtain_user


@app.route('/', strict_slashes=False)
def index():
    """
    Render html page from external resource
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True
    )
