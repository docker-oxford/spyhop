#!/usr/bin/env python

import os
import json
import argparse

from flask import Flask, jsonify

from api import Api

socket = os.getenv('DOCKER_HOST', 'unix://var/run/docker.sock')

# Get command line arguments
parser = argparse.ArgumentParser(description='Run Spyhop')
parser.add_argument('-H', '--host', default=socket,
                    help='Socket on which to talk to Docker Daemon')
parser.add_argument('-p', '--port', type=int, default=5000,
                    help='Port for web server to listen on')
args = parser.parse_args()

# Create API connection
docker_api = Api(args.host)

# Create Flask app
app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/ps')
def ps():
    all_containers = docker_api.get_all_containers()
    return jsonify({"data": all_containers})


@app.route('/api/<container_id>')
def stats(container_id):
    container_stats = docker_api.get_container_stats(container_id)
    return jsonify(json.loads(container_stats.next()))


@app.route('/api/curated/<container_id>')
def curated_stats(container_id):
    stats = docker_api.get_curated_stats(container_id)
    return jsonify(stats)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port, debug=True)
