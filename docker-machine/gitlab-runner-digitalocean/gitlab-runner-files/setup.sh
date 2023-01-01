#!/usr/bin/env bash
set -euxo pipefail

# Run this on the node meant to host GitLab Runners.

docker-compose exec gitlab-runner-container \
    gitlab-runner register \
    --non-interactive \
    --url $YOURGITLABURL \
    --registration-token $YOURGITLABREGISTRATIONTOKEN \
    --executor docker \
    --description "Sample Runner 1" \
    --docker-image "docker:stable" \
    --docker-volumes /var/run/docker.sock:/var/run/docker.sock
