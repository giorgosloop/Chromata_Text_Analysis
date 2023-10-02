import pymongo
from bson.json_util import dumps
import time
import json
from text_generation import text_generation

# This code listen to changes of the MongoDB collection and triggers the text-generation code

# Connect to MongoDB
client = pymongo.MongoClient('')   # Need to add a specific value here!!
print("[INFO] Connected to MongoDB!")

print("[INFO] ******* Text-generation listener is ready!")

# Listen to changes in InputQueue collection
change_stream = client.ImagesDB.Chromata_InputQueue_TG.watch()  # May need adaptation.
for change in change_stream:

    request = dumps(change)
    json_request = json.loads(request)
    json_keys = json_request.keys()
    print("\n\n [INFO] ******* Received a new request: \n")

    print(json_keys)

    if "fullDocument" in json_keys:
        print(json_request["fullDocument"])

        text_generation(json_request["fullDocument"])
      
    print("\n[INFO] ******* Text-generation listener is ready!")
