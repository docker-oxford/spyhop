#!/usr/bin/env python
from docker import Client
from flask import jsonify
import json


def calculate_cpu_percent(stats_generator):
    # Get one stat
    stat1 = json.loads(stats_generator.next())
    cpu1 = stat1['cpu_stats']['cpu_usage']['total_usage']
    system1 = stat1['cpu_stats']['system_cpu_usage']
    # Get another
    stat2 = json.loads(stats_generator.next())
    cpu2 = stat2['cpu_stats']['cpu_usage']['total_usage']
    system2 = stat2['cpu_stats']['system_cpu_usage']
    # Calculate deltas
    cpu_delta = float(cpu2 - cpu1)
    system_delta = float(system2 - system1)
    # Calculate percent
    if (system_delta > 0.0 and cpu_delta > 0.0):
        cpu_percent = (cpu_delta / system_delta) * len(stat2['cpu_stats']['cpu_usage']['percpu_usage']) * 100.0
    else:
        cpu_percent = 0.0

    if cpu_percent < 150:
        return cpu_percent
    else:
        return 0.0

def get_container_stats(container_id):
    cli = Client(base_url='unix://var/run/docker.sock')
    try:
        stats = cli.stats(container_id)
        return stats
    except Exception, error:
        return error

def get_curated_stats(container_id):
    stats_generator = get_container_stats(container_id)
    cpu_percent = calculate_cpu_percent(stats_generator)
    monitoring_stats = {"cpu_percent": cpu_percent}
    return monitoring_stats

def get_all_containers():
    cli = Client(base_url='unix://var/run/docker.sock')
    containers = cli.containers()
    return containers


def main():
    pass

if __name__ == '__main__':
    main()

