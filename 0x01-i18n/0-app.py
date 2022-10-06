#!/usr/bin/env python3
"""This module contains a basic Flask app to jumpstart the application
This contains each of the app routes for the web application"""

from unicodedata import name
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slahes=False)
def index():
    """Simple message"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
