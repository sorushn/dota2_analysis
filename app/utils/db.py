from pymongo import MongoClient


def save_matches(matches: list):
    db = get_database()
    collection = db.matches
    collection.insert_many(matches)
    client.close()


def get_database(dbname="dota"):
    client = MongoClient("mongodb://mongodb:27017/")
    db = client[dbname]
    return db
