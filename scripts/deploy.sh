#!/bin/bash
docker login -u ${docker_username} -p ${docker_password}
docker tag noderrobot/core:build-${TRAVIS_JOB_ID} noderrobot/core:build-${TRAVIS_JOB_ID}
docker push noderrobot/core:build-${TRAVIS_JOB_ID}
docker logout