#!/bin/bash

# Completely Build
docker buildx build $(cat .devpass.env | sed 's@^@--build-arg @g' | paste -s -d " " /dev/stdin) --progress=plain --no-cache --pull -t azymik/flask--udemy-course-rest-api-with-flask-and-python-in-2024--your-first-rest-api .

# Build with Cache
# docker buildx build $(cat .devpass.env | sed 's@^@--build-arg @g' | paste -s -d " " /dev/stdin) --progress=plain -t azymik/flask--udemy-course-rest-api-with-flask-and-python-in-2024--your-first-rest-api .

# Start Container
docker container run -it --rm -v ./:/app -p 65000:5000 azymik/flask--udemy-course-rest-api-with-flask-and-python-in-2024--your-first-rest-api
