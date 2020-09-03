#!/usr/bin/python3
"""states template
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def current_remove(self):
    """request you must close the current SQLAlchemy Session
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_html():
    """display states by city
    """
    data = storage.all("State")
    return render_template('8-cities_by_states.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
