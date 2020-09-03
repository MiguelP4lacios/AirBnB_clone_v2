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

# host:5000/(id)
@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_html(id):
    """display states Id
    """
    data = storage.all("State")
    return render_template('9-states.html', states=data, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug='True')
