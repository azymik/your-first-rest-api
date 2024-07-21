#!/bin/bash

# Development
# flask run --host=0.0.0.0

# Production
gunicorn --bind 0.0.0.0:80 'app:create_app()'