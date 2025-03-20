from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


def get_collection(database, collection):
    USER = os.getenv("MONGO_USER")
    PASSWORD = os.getenv("MONGO_PASSWORD")

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(
        host="localhost",
        port=27017,
        username=os.getenv("MONGO_USER"),
        password=os.getenv("MONGO_PASSWORD"),
        authSource="admin",
    )
    database = client[database]
    collection = database[collection]
    return collection



if __name__ == "__main__":
    profiles = get_collection("linkedin", "profiles")
    print(profiles)


