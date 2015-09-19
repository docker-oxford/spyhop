#!/usr/bin/env python
from docker import Client

def get_container_stats(container_id):
    cli = Client(base_url='unix://var/run/docker.sock')
    stats = cli.stats(container_id)
    return stats

def main():
    container_id = 'db72a8931dcd'
    stats = get_container_stats(container_id)
    for stat in stats:
        print(stat)

if __name__ == '__main__':
    main()

