#!/usr/bin/env bash

echo "docker run Started ...."

podman run -d -p 3001:3001 --name my-aaa \
    --env LOGLEVEL=DEBUG \
    -v "/Users/gandhi/GandhiMain/700-Apps/envizi-integration-hub/app/config.json:/app/config.json" \
    gandigit/aaaa:latest

echo "run completed ...."