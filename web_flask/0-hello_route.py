#!/usr/bin/python3
"""Module welcome to flask
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
        """index function

        Returns:
            [string]: [message]
        """
        return "Hello HBNB!\n"


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
