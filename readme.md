# Flask course 'REST APIs with Flask and Python in 2024'

### .vscode folder
Contain configuration file for vscode

### instance folder
Database folder, can be deleted to re-initialize

### migrations folder
Database migrations folder, can be deleted to re-initialize

## Endpoints
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