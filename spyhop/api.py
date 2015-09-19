#!/usr/bin/env python
from docker import Client

def get_container_stats(container_id):
    cli = Client(base_url='unix://var/run/docker.sock')
    try:
        stats = cli.stats(container_id)
        return stats
    except Exception, error:
        return error

def get_all_containers():
    cli = Client(base_url='unix://var/run/docker.sock')
    containers = cli.containers()
    return containers

def main():
    pass

if __name__ == '__main__':
    main()

