#!/usr/bin/python3

'''script that starts a Flask web application
'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def current_remove(self):
    """
    request you must remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_html():
    """
    display a HTML page
    """
    data = storage.all("State")
    return render_template('7-states_list.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
