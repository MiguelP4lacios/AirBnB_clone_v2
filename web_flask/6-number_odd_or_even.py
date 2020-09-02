#!/usr/bin/python3
"""Module add route
"""

from flask import Flask, render_template

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
    """number function
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """number template function
    """
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """number template function
    """
    even = lambda num: n%2 == 0
    return render_template("6-number_odd_or_even.html", num=n, even=even(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
