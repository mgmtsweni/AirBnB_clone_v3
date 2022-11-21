#!/usr/bin/python3
"""Connect to API"""
from flask import Flask, Blueprint
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask('app')
app.register.blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(self):
    """teardown_appcontext"""
    storage.close()


if __name__ == '__main__':
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')

    host = '0.0.0.0' if not HBNB_API_HOST else HBNB_API_HOST
    port = 5000 if not HBNB_API_PORT else HBNB_API_PORT
    app.run(host=host, port=port, threaded=True)
