import json
from pathlib import Path
from pprint import pprint
from connect_mongodb import get_collection
from pymongo.errors import DuplicateKeyError, BulkWriteError


def read_json(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)

    return data


def insert_profile_records(collection, data):
    collection.create_index("user_id", unique=True)
    collection.insert_many(data)


if __name__ == "__main__":
    profiles_path = Path(__file__).parent / "linkedin_profiles.json"
    profiles_data = read_json(profiles_path)

    profile_collection = get_collection("linkedin", "profile")
    try:
        insert_profile_records(profile_collection, profiles_data)
    except (DuplicateKeyError, BulkWriteError) as err:
        print(err)