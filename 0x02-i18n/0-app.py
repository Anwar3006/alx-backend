#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render html page from external source
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(
        'localhost',
        5000,
        True
    )
