#!/usr/bin/env python3
"""This module contains a basic Flask app to jumpstart the application
This contains each of the app routes for the web application"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Class for the config obj"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """Get user info from request"""
    user = request.args.get('login_as')
    try:
        return users.get(int(user))
    except Exception:
        return None


@app.before_request
def before_request():
    """Before request to save the user into database"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Function to get locale selection"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    try:
        user = get_user()
        if (user and user['locale'] and
           user['locale'] in app.config['LANGUAGES']):
            return user['locale']
    except Exception:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Simple message"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
