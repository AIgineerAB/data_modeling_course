from connect_postgres import connect_postgres
from sqlalchemy import text

username = input("Enter username:")
password = input("Enter password:")

with connect_postgres().connect() as conn:
    result = conn.execute(text(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"))

    if result.fetchall():
        print("login success")
        print(f"You can now eat all ice cream you want")
    else: 
        print("another failure, try again")


# postgres don't allow multiple statements, but mysql does 
# DROP TABLE users;--

# alice' OR '1'='1
# ' OR '1'='1' --     