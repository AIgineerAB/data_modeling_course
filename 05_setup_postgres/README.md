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

>[!Tips]
>Work on [this exercise](https://github.com/AIgineerAB/data_platform_course/blob/main/exercises/exercise_2.md) to strengthen your knowledge on Docker fundamentals.

## 2. PostgreSQL
Now, we will be spinning up a PostgreSQL container via Docker and connect it in the terminal. 

<a href="https://youtu.be/fo_C6MSmtkQ" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_platform/postgres.png?raw=true" alt="postgres" width="600">
</a>

>[!Note]
>CORRECTION TO THE VIDEO: due to a latest postgreSQL version, the volume path in the `docker-compose` file should be updated to `postgres_data:/var/lib/postgresql`. 

### .env file
Start with creating a .env in your folder and fill in information for your postgres setup:

```bash
POSTGRES_HOST="localhost"
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="your_supersafe_password" # NOTE: change this
POSTGRES_DB="myh_db"
POSTGRES_PORT=5432
```

### docker compose

Now place a docker-compose.yml file in your root also. You can take the same docker-compose.yml that is under this lecture folder.

Run

```bash
docker compose up -d
```

to spin up the postgres container. If it doesn't work, make sure to

- be in the correct folder where you docker-compose.yml file is
- clean up old containers and old volumes

### Interact with postgreSQL via Terminal
Go into your postgres container with

```bash
docker exec -it postgres bash
```

```bash
psql -U your_username -d your_database
```

> [!NOTE]
> The password is not required when connecting to postgres locally i.e. inside of the container. When connecting from the host machine directly it will require a password. This is the default settings of postgres.

### Interact with postgreSQL via python
Check out the jupyter notebook under this lecture folder. The juypter notebook requires the python packages below. Install them using `uv`.

```cmd
ipykernel openpyxl pandas psycopg2-binary python-dotenv sqlalchemy
```

### DDL with postgreSQL (To be upated)

## Read more 👓

- [Using PostgreSQL SERIAL to Create Auto-increment Column - postgres tutorial NEON](https://neon.tech/postgresql/postgresql-tutorial/postgresql-serial)
