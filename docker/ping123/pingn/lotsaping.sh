#!/usr/bin/env bash

ROOT_PING=1 APP_NAME=ping1 PORT=5001 pipenv run python pingn.py > "ping1.log" 2>&1 &

for i in {2..20} ; do
  ((h=i-1))

  APP_NAME="ping$i" PORT="500$i" CHILD_URL="http://localhost:500$h" CHILD_NAME="ping$h" pipenv run python pingn.py > "ping$i.log" 2>&1 &
done

echo "tail ping$i.log"
tail "ping$i.log"
