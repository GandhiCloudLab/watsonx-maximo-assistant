#!/usr/bin/env bash

cd ..

podman run --env-file .env -d -p 8080:8080 --name wx-wa-python1 docker.io/gandigit/wx-wa-python2

podman logs wx-wa-python1