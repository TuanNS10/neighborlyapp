import azure.functions as func
import pymongo
from bson.objectid import ObjectId

from config import MONGODB_CONNECTION_STRING, MONGODB_NAME, ADS_COLLECTION


def main(req: func.HttpRequest) -> func.HttpResponse:
    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url = MONGODB_CONNECTION_STRING
            client = pymongo.MongoClient(url)
            database = client[MONGODB_NAME]
            collection = database[ADS_COLLECTION]

            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)
