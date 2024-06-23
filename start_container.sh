#!/bin/bash
code .
docker buildx build --build-arg devpass=1234 --progress=plain -t azymik/flask--udemy-course-rest-api-with-flask-and-python-in-2024--your-first-rest-api .
docker container run -it --rm -v ./:/app -p 65000:5000 azymik/flask--udemy-course-rest-api-with-flask-and-python-in-2024--your-first-rest-api
