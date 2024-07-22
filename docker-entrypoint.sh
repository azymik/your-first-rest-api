#!/bin/sh

/home/devuser/.venv/bin/flask db init
/home/devuser/.venv/bin/flask db upgrade

exec /home/devuser/.venv/bin/flask run --host=0.0.0.0
# exec /home/devuser/.venv/bin/gunicorn --bind 0.0.0.0:80 'app:create_app()'