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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display a HTML page like 6-index.html, 0x01. AirBnB clone
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug='True')