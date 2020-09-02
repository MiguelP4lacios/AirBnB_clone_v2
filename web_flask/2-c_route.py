#!/usr/bin/python3
"""Module add route
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """index function
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def f_hbnb():
    """hbnb function
    """
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def parm_hbnb(text):
    """c function
    """
    return "C " + text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
