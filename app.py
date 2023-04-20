from bson.objectid import ObjectId
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/RecipeSuggestionSystem"
mongo = PyMongo(app)
app.secret_key = "DEV"


@app.route("/", methods=["GET", "POST"])
def home():
    # documentsCount = mongo.db.Recipes.count_documents({})
    documents = mongo.db.Recipes.find({}).limit(100)
    if request.method == "POST":
        app.logger.debug(f"Ingredients: {request.form['ingredients']}")
        print(f"{list([request.form['ingredients']])}")
        result = mongo.db.Recipes.find_one(
            {"ingredients": {"$in": list([request.form["ingredients"]])}}
        )
        return f"{result}"
    return render_template("index.html", documents=documents)


@app.route("/recipe/<_id>")
def recipe(_id):
    recipe = mongo.db.Recipes.find_one({"_id": ObjectId(_id)})
    return render_template("recipe.html", recipe=recipe, _id=_id)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if "username" in session:
        return render_template("admin.html")
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("admin"))
    if request.method == "POST":
        username = request.form["username"]
        app.logger.debug(username)
        password = request.form["password"]
        app.logger.debug(password)
        error = None
        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        if error is None:
            session.clear()
            session["username"] = request.form["username"]
            return redirect(url_for("admin"))
        flash(error)
    redirect(url_for("admin"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return "Logged out."


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        if error is None:
            if mongo.db.Users.find_one({"username": username}) is not None:
                error = f"User {username} is already registered."
            else:
                mongo.db.Users.insert_one(
                    {"username": username, "passwordHash": generate_password_hash}
                )
                return redirect(url_for("admin"))
        flash(error)
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
