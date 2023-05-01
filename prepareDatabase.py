import json

import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["RecipeSuggestionSystem"]
    collection = db["Recipes"]

    for idx, document in enumerate(collection.find()):
        print(idx, document["_id"])
        collection.update_one({"_id": document["_id"]}, {
            "$set": {
                "ingredients":
                json.loads(json.dumps(eval(str(document["ingredients"])))),
                "steps":
                json.loads(json.dumps(eval(str(document["steps"])))),
                "tags":
                json.loads(json.dumps(eval(str(document["tags"]))))
            }
        })
