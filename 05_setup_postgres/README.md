# Implementation on postgreSQL

We'll be using docker to spin up a postgresql instance and create a DB inside it according to a physical model as the blueprint. 


## 1. Docker
Docker lets us quickly spin up an isolated PostgreSQL environment that behaves the same on every machine, making setup simple and reliable. It is especially important for data engineering pipelines because it ensures reproducible environments in your workflow. First, we will set up docker and learn about the fundamentals of Docker: 

### 1a. Set up 
Follow the video in the link to set up docker on your computer according to your OS [Video Instruction](https://github.com/AIgineerAB/data_platform_course/tree/main/04_setup_docker)

### 1b. Docker image
A Docker image provides the blueprint for your environment, guaranteeing that everyone runs the exact same setup. [Video Instruction](https://github.com/AIgineerAB/data_platform_course/tree/main/05_docker_image)

### 1c. Docker compose 
A Docker Compose file lets you define and run multi‑container systems with a single command. It is commonly used in more complex pipelines. [Video Instruction](https://github.com/AIgineerAB/data_platform_course/tree/main/06_docker_compose)

> [!TIP]
> Work on [this exercise](https://github.com/AIgineerAB/data_platform_course/blob/main/exercises/exercise_2.md) to strengthen your knowledge on Docker fundamentals.


## 2. PostgreSQL
Now, we will be spinning up a PostgreSQL container via Docker and connect it in the terminal. Follow the video below for this and check the notes to the video below. 

<a href="https://youtu.be/fo_C6MSmtkQ" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_platform/postgres.png?raw=true" alt="postgres" width="600">
</a>

> [!Note]
> - CORRECTION TO THE VIDEO: due to a latest postgreSQL version, the volume path in the `docker-compose` file should be updated to `postgres_data:/var/lib/postgresql`
> - OPTIONAL CONTENTS IN THE VIDEO: the part of python interaction in the video (which is from *8:30-19:45*) is optional for this course. If you are interested, you needs the python packages below. Otherwise, you can skip this part of the video:
>   ```cmd
>   ipykernel openpyxl pandas psycopg2-binary python-dotenv sqlalchemy
>   ```

Below are notes to the instructions covered in the video above:
### 2a. Adding .env file
Start with creating a .env in your folder and fill in information for your postgres setup:

```bash
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="your_supersafe_password" # NOTE: change this
POSTGRES_DB="myh_db"
POSTGRES_PORT=5432
```

### 2b. Docker compose

Now place a docker-compose.yml file in your root also. You can take the same docker-compose.yml that is under this lecture folder.

Navigate to the directory *05_setup_postgres* in the terminal and run to spin up the postgres container: 
```bash
docker compose up -d
```

If it doesn't work, make sure to
- be in the correct folder where you docker-compose.yml file is
- clean up old containers and old volumes

### 2c. Interact with postgreSQL in the container
When the container is running, you can *step inside* your postgres container with the commands below.

#### Use bash shell
To run commands inside an already running container, interactively via the terminal of the host machine:
```bash
docker exec -it postgres bash
```

Afterwards, you can run bash commands like `ls`, `cd` etc in the container. Use `exit` to terminate the session. 

> [!Note]
> Note that in the latest version of postgreSQL in the docker image, the folder structure of the postgreSQL software is different than the one shown on the video. Now, the postgreSQL files are stored in this path in the container's root directory:
> ```/var/lib/postgresql/18/docker/```

#### Use postgreSQL CLI
Run the command below to open a `psql` session:
```bash
psql -U your_username -d your_database
```

You can then run `psql` commands to interact with your postgreSQL instance. Here are some common `psql` commands:
| Command                   | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| `\l`                      | List all databases                                        |
| `\i <path_to_sql_script>` | To read a an SQL file                                     |
| `\c database_name`        | Connect to a specific database                            |
| `\dt`                     | List all tables in the current database                   |
| `\d table_name`           | Show table structure (columns, types, constraints)        |
| `\du`                     | List all users and roles                                  |
| `\conninfo`               | Show current connection info (user, database, host, port) |
| `\q`                      | Quit `psql`                                               |


> [!NOTE]
> The password is not required when connecting to postgres locally i.e. inside of the container. When connecting from the host machine directly it will require a password. This is the default settings of postgres.

### 2d. Running *.sql* files with postgreSQL in the container

Use the `psql \i` command to run a simple DDL and DML queries stored in the `sql` subfolder under this lecture. You should be able to see a table created under the postgresql DB and then a row inserted into it. 

> [!NOTE]
> Now choose a physical model that you have worked with and create corresponding `.sql` files for DDL queries. Then run the files in the postgreSQL instance via container. Are you able to create tables according to you physical model?


## Read more 👓
- [Using PostgreSQL SERIAL to Create Auto-increment Column - postgres tutorial NEON](https://neon.tech/postgresql/postgresql-tutorial/postgresql-serial)
