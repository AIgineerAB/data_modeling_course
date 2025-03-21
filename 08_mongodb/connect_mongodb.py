from pymongo import MongoClient
from dotenv import load_dotenv
import os


def get_collection(database_name, collection):
    load_dotenv()

    USER = os.getenv("MONGO_USER")
    PASSWORD = os.getenv("MONGO_PASSWORD")

    client = MongoClient(
        host="localhost",
        port=27017,
        username=USER,
        password=PASSWORD,
        authSource="admin",
    )

    database = client[database_name]
    collection = database[collection]
    return collection


if __name__ == "__main__":
    profiles = get_collection("linkedin", "profiles")
    # profiles.insert_one({"userid": 83192038})
    print(profiles)

