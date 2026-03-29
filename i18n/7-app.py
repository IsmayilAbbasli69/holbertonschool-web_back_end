#!/usr/bin/env python3
"""7-app.py"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_TRANSLATION_DIRECTORIES = 'translations'


app = Flask(__name__)
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


def get_timezone():
    """Determine the best match with our supported timezones."""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            try:
                pytz.timezone(timezone)
                return timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


babel = Babel(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone
)


@app.route('/')
def index():
    """Render the index template"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
