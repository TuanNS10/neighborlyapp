import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

from config import MONGODB_CONNECTION_STRING, MONGODB_NAME, POSTS_COLLECTION


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = MONGODB_CONNECTION_STRING
        client = pymongo.MongoClient(url)
        database = client[MONGODB_NAME]
        collection = database[POSTS_COLLECTION]

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)