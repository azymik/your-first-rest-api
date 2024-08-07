# Flask course 'REST APIs with Flask and Python in 2024'

### .vscode folder
Contain configuration file for vscode

### instance folder
Database folder, can be deleted to re-initialize

### migrations folder
Database migrations folder, can be deleted to re-initialize

### devpass.env
dev password, used for admin password in Dockerfile

### app.py
Contain `JWT_SECRET_KEY` and `SQLALCHEMY_DATABASE_URI`

### Dockerfile
`EXPOSE 5000` is required for DEV, can be removed in PROD

## Build/Start Container
### Build without Cache
```
docker buildx build $(cat .devpass.env | sed 's@^@--build-arg @g' | paste -s -d " " /dev/stdin) --progress=plain --no-cache --pull -t azymik/flask--udemy-course-rest-api-with-flask-and-python-in-2024--your-first-rest-api .
```

### Build with Cache
```
docker buildx build $(cat .devpass.env | sed 's@^@--build-arg @g' | paste -s -d " " /dev/stdin) --progress=plain -t azymik/flask--udemy-course-rest-api-with-flask-and-python-in-2024--your-first-rest-api .
```

### Start Container
Use `flask run` for DEV, `gunicorn` for PROD (edit in `docker-entrypoint.sh`)
```
docker compose up -d
```

inside `web` container, run line below, in order to run `rq worker` to run subtasks in the background, -u for url, then follow by tasks name
```
rq worker -u redis://redis_db:6379 tasks
```

## Initializing/Migrating/Upgrading Database
After first deploy, do `init`, `migrate` and `upgrade`

Subsequently, Migrate then Upgrade everytime that models change

After migrate, check `migrations/versions` before upgrade
```
docker compose exec web /home/devuser/.venv/bin/flask db init
docker compose exec web /home/devuser/.venv/bin/flask db migrate
docker compose exec web /home/devuser/.venv/bin/flask db upgrade
```

To check database
```
docker compose exec -it db psql -U postgres -W myapp
```

## Endpoints
Use `httpie` for testing
port = 5000 DEV `flask run --host=0.0.0.0` | 80 PROD `gunicorn --bind 0.0.0.0:80 'app:create_app()'`

### item.py
```
http GET :[port]/item/[item_id] 'Authorization:Bearer [access_token]'
http DELETE :[port]/item/[item_id] 'Authorization:Bearer [access_token]'
http PUT :[port]/item/[item_id] name='[item_name]' price:=[item_price]

http GET :[port]/item 'Authorization:Bearer [access_token]'
http POST :[port]/item name='[item_name]' price:=[item_price] store_id:=[store_id] 'Authorization:Bearer [access_token]'
```

### store.py
```
http GET :[port]/store/[store_id]
http DELETE :[port]/store/[store_id]

http GET :[port]/store
http POST :[port]/store name='[store_name]'
```

### tag.py
```
http GET :[port]/store/[store_id]/tag
http POST :[port]/store/[store_id]/tag name='[tag_name]'

http POST :[port]/item/[item_id]/tag/[tag_id]
http DELETE :[port]/item/[item_id]/tag/[tag_id]

http GET :[port]/tag/[tag_id]
http DELETE :[port]/tag/[tag_id]
```

### user.py
```
http POST :[port]/register username=[username] password=[password]

http POST :[port]/login username=[username] password=[password]

http POST :[port]/refresh 'Authorization:Bearer [refresh_token]'

http POST :[port]/logout 'Authorization:Bearer [access_token]'

http GET :[port]/user/[user_id]
http DELETE :[port]/user/[user_id]
```
