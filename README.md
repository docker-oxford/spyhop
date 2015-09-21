![spyhop](spyhop.png)

# spyhop
Container monitoring web UI inspired by [docker-mon](https://github.com/icecrime/docker-mon).

## Features

* List all containers running on a host
* See CPU utilisation for each container

## Limitations/Todos

This is a work in progress with a long list of limitations to fix. Listing some of the major ones here.

* Can we/do we want Spyhop to run inside a container?
* Monitoring a single container instead of all in one graph
* Ability to switch between containers by clicking the names in the list
* Multiple views on the same page: cpum, mem, rx and tx (served by back-end)
* Host metrics as overlay
* Get metrics from multiple hosts
