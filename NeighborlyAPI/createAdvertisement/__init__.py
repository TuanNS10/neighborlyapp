
import azure.functions as func
import pymongo

from config import MONGODB_CONNECTION_STRING, MONGODB_NAME, ADS_COLLECTION


def main(req: func.HttpRequest) -> func.HttpResponse:
    request = req.get_json()

    if request:
        try:
            url = MONGODB_CONNECTION_STRING
            client = pymongo.MongoClient(url)
            database = client[MONGODB_NAME]
            collection = database[ADS_COLLECTION]

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
