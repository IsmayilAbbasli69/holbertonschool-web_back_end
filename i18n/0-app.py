#!/usr/bin/env python3
"""
Basic Flask application module.
This module initializes a Flask instance and defines a single route
for the index page of the application.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles the root route '/'.
    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
