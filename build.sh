#!/bin/sh

poetry update
poetry build
tar -xvf $1 --wildcards --no-anchored '*/setup.py' --strip=1
poetry build
tar -xvf $1 --wildcards --no-anchored '*/setup.py' --strip=1