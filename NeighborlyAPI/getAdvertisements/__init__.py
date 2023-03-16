import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

from config import MONGODB_CONNECTION_STRING, MONGODB_NAME, ADS_COLLECTION


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        url = MONGODB_CONNECTION_STRING
        client = pymongo.MongoClient(url)
        database = client[MONGODB_NAME]
        collection = database[ADS_COLLECTION]

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)
