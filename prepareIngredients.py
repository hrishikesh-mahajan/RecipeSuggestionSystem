import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['RecipeSuggestionSystem']
    collection = db['Recipes']

    ingredientsSet = set()
    for document in collection.find():
        ingredientsSet.update(set(document["ingredients"]))

    print("Total Ingredients:", len(ingredientsSet))

    ingredientsSet = sorted(ingredientsSet)

    ingredientsList = [
        ingredient for ingredient in ingredientsSet if len(ingredient) > 1]

    with open('ingredients.py', 'w') as f:
        f.write("ingredientsList = " + str(ingredientsList))
