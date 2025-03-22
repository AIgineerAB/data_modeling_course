from connect_postgres import connect_postgres
from sqlalchemy import text

username = input("Enter username:")
password = input("Enter password:")

with connect_postgres().connect() as conn:
    result = conn.execute(
        # :parameter - parameterized bind - SQLAlchemy tells database driver (psycopg2) to make parameterized statements
        # and sends the data in separately, they will be treated as string literals 
        # conn.execute("SELECT * FROM users WHERE username = %s AND password = %s", ("alice", "pass123"))


        text("SELECT * FROM users WHERE username = :username AND password = :password"),
        {"username": username, "password": password},
    )

    if result.fetchall():
        print("login success")
        print(f"You can now eat all ice cream you want")
    else:
        print("another failure, try again")


# TODO: implement security measures against SQL injections
