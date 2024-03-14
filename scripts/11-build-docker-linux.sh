#!/usr/bin/env bash

echo "build Started ...."

cd ..
podman build --platform linux/amd64 -f Dockerfile -t docker.io/gandigit/wx-wa-python2:latest .
# podman push docker.io/gandigit/wx-wa-python2:latest

echo "build completed ...."

