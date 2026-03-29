#!/usr/bin/env python3
"""6-app.py"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_TRANSLATION_DIRECTORIES = 'translations'


app.config.from_object(Config)


def get_user():
    """Get user from request"""
    login_as = request.args.get('login_as')
    if login_as is None:
        return None
    try:
        return users.get(int(login_as))
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """Set user in g"""
    g.user = get_user()


def get_locale():
    """Determine the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Render the index template"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
