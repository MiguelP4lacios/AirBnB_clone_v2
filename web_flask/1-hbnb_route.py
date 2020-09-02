#!/usr/bin/python3
"""Module add route
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
        """index function

        Returns:
            [string]: [message]
        """
        return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def f_hbnb():
        """hbnb function

        Returns:
            [string]: [message]
        """
        return "HBNB!"


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
