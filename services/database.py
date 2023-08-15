import logging

import pymongo
from pymongo.server_api import ServerApi

uri = "mongodb+srv://freeDb:free1234@cluster0.oxfxzv2.mongodb.net/?retryWrites=true&w=majority"


def db_init():
    client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
    return client.test


def validate_collections(db):
    try:
        collections = db.collection_names(include_system_collections=False)
        for collection in collections:
            db.validate_collection(collection)
        logging.info('Validation successfull...')
    except Exception as err:
        logging.error(f"Failed to validate database collection: {err}")


db = db_init()
