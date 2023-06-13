#!/usr/bin/env bash
set -euxo pipefail

JENKINS_DATA_DIR=./jenkinsData/
JENKINS_DATA_DIR=`realpath $JENKINS_DATA_DIR`

mkdir -p jenkinsData
docker run \
  -p 8080:8080 \
  -p 50000:50000 \
  --volume $JENKINS_DATA_DIR:/var/jenkins_home \
  jenkinswithtools:1.0.0