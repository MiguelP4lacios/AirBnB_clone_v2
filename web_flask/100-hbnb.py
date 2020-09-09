#!/usr/bin/python3
"""states template
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def current_remove(self):
    """request you must remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display a HTML page like 8-index.html, 0x01. AirBnB clone
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug='True')
