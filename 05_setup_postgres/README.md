# Setup postgres

TODO: video
<!-- <a href="" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/FOLDER_NAME/.png?raw=true" alt="DESCRIPTION" width="600">
</a> -->


We'll be using docker and docker compose to run postgresql. Then we'll use postgresql explorer extension in vscode to run postgres directly from vscode instead of relying on pgadmin, dbeaver or similar IDEs. 

## Setup 

Place a .env file in the root of your repository. We will use the same postgres database with different schemas to logically group different lectures and exercises.

Your .env file should contain 

```bash
POSTGRES_HOST="localhost"
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="your_supersafe_password" # NOTE: change this
POSTGRES_DB="data_modeling_course_db"
POSTGRES_PORT=5432
```

Now place a docker-compose.yml file in your root also. You can take the same docker-compose.yml that is under this lecture folder. 



## Other videos 📹

## Read more 👓
