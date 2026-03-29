#!/usr/bin/env python3
"""3-app.py"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_TRANSLATION_DIRECTORIES = 'translations'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """Determines supported lang."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def main_page():
    """Main page route that renders the index template"""
    return render_template('3-index.html'), 200


if __name__ == '__main__':
    app.run()
