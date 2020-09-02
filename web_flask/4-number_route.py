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


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """c function
    """
    return "C {}".format(text).replace("_", " ")


# host:5000/python/(text)
@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is_cool"):
    """python function
    """
    return "Python {}".format(text).replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """python function
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
