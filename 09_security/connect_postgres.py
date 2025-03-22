from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os


def connect_postgres():
    load_dotenv()

    db_user = os.getenv("POSTGRES_USER")
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_name = os.getenv("POSTGRES_DB")

    postgres_connection = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )

    return postgres_connection


if __name__ == "__main__":
    conn = connect_postgres()
    with conn.connect() as connection:
        result = connection.execute(text("SELECT * FROM INFORMATION_SCHEMA.SCHEMATA;"))
        print(result.fetchall())
