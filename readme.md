.vscode: VS Code Configuration Directory
- settings.json: VS Code Configuration JSON File

instance: DB Directory
- data.db: DB File

migrations: DB Migrations Info Directory
- many files

models: Model Directory
- item.py
- store.py

resources: API Directory
- item.py
- store.py

\
.devpass.env: Password for docker 'devuser' account\
\
.flask.env: Environment for Flask\
\
.gitignore\
\
app.py: Starting Point for Flask\
\
blocklist.py: Contains blocklist of JWT tokens which added after user logged out\
\
db.py: Setting Up Database\
\
Dockerfile\
\
initialize_db.sh: Initialize database\
\
readme.md\
\
requirements.txt: Python required packages list\
\
run_flask.sh: Shell Script to run Flask\
\
schemas.py: Schema for API\
\
start_container.sh: Shell Script to Create Image, Run Container for Flask