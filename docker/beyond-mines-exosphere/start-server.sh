#!/usr/bin/env bash

if [ ! -d ./minecraft-data/ ]; then
  mkdir -p ./minecraft-data/
fi

docker run \
  --interactive \
  --tty \
  --mount type=bind,source=./minecraft-data/,target=/minecraft/ \
  --name beyondminesexosphere \
  beyondminesexosphere:2.0.2
