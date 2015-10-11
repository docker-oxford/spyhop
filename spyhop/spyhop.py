#!/usr/bin/env python
from flask import Flask, jsonify
import argparse
import os
from api import Api
import json

app = Flask(__name__)

# Get command line arguments
parser = argparse.ArgumentParser(description='Run Spyhop')
parser.add_argument('-H', '--host', metavar='HOST', type=str, nargs='?', default=os.getenv('DOCKER_HOST', 'unix://var/run/docker.sock'),
                   help='Socket on which to talk to Docker Daemon')
args = parser.parse_args()
host = args.host

# Create API connection
docker_api = Api(host)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/<container_id>')
def stats(container_id):
    container_stats = docker_api.get_container_stats(container_id)
    return jsonify(json.loads(container_stats.next()))

@app.route('/api/curated/<container_id>')
def curated_stats(container_id):
    stats = docker_api.get_curated_stats(container_id)
    return jsonify(stats)

@app.route('/api/ps')
def ps():
    all_containers = docker_api.get_all_containers()
    return jsonify({"data": all_containers})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
