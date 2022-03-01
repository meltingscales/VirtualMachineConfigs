#!/usr/bin/env bash

ROOT_PING=1 APP_NAME=ping1 PORT=5001 pipenv run python -m pingn > "ping1.log" 2>&1 &

for i in {2..20} ; do
  ((h=i-1))
  ((port=500+h))

  APP_NAME="ping$i" PORT="500$i" CHILD_URL="http://localhost:$port" CHILD_NAME="ping$h" pipenv run python -m pingn > "ping$i.log" 2>&1 &
done

echo "tail ping$i.log"
tail "ping$i.log"
