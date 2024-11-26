import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["RecipeSuggestionSystem"]
    collection = db["Recipes"]
    documents = collection.find({})
    print(client)
    # for item in documents:
    #     print(item)
    print(len(list(documents)))
