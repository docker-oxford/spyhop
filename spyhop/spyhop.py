#!/usr/bin/env python
from flask import Flask, jsonify
from api import get_container_stats
import json

app = Flask(__name__)

@app.route('/api/<container_id>')
def stats(container_id):
    container_stats = get_container_stats(container_id)
    return jsonify(json.loads(container_stats.next()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
