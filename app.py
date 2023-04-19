from bson.objectid import ObjectId
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/RecipeSuggestionSystem"
mongo = PyMongo(app)


@app.route("/")
def home():
    # documentsCount = mongo.db.Recipes.count_documents({})
    documents = mongo.db.Recipes.find({}).limit(100)
    return render_template("index.html", documents=documents)


@app.route("/<_id>")
def recipe(_id):
    recipe = mongo.db.Recipes.find_one({"_id": ObjectId(_id)})
    return render_template("recipe.html", recipe=recipe, _id=_id)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
