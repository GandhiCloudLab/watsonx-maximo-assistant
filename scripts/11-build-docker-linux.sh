#!/usr/bin/env bash

echo "build Started ...."

cd ..
podman build --platform linux/amd64 -f Dockerfile -t docker.io/gandigit/maixmo-db-interface:latest .

echo "build completed ...."

