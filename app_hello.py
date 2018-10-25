#!/usr/bin/python

import os

from flask import Flask, g, render_template


app = Flask(__name__)  # pylint: disable=invalid-name
app.config.from_pyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.py'))


@app.route('/')
def hello():
    return render_template(os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates/network_display.html'))

@app.route('/bye')
def bye():
    return "bye now"

@app.route('/wifi_presence')
def wifi_presence():
    return "bye now"


'''
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = DB(app.config)
    return db
'''

@app.teardown_appcontext
def close_connection(_):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8283)
