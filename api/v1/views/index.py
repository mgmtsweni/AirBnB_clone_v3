#!/usr/bin/python3
"""Index for connecting to the API"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """Returns a status """
    return jsonify(status="OK")
