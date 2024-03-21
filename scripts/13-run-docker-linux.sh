#!/usr/bin/env bash

cd ..

podman run --env-file .env -d -p 8080:8080 --name maixmo-db-interface docker.io/gandigit/maixmo-db-interface

podman logs maixmo-db-interface