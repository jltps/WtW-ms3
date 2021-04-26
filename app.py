import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    flash("This is a flash test")
    return render_template("home.html")


@app.route("/browse")
def get_titles():
    titles = list(mongo.db.titles.find())
    return render_template("browse.html", titles=titles)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration successful. Welcome {}".format(
            request.form.get("username")))
        return redirect(url_for("browse"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(request.form.get("username")))
                return redirect(url_for("get_titles"))
            else:
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/add_title", methods=["GET", "POST"])
def add_title():
    if request.method == "POST":
        all_ages = "yes" if request.form.get("all_ages") else "no"
        title = {
            "title_name": request.form.get("title_name"),
            "type_name": request.form.get("title_types"),
            "genre_name": request.form.get("genres"),
            "platform_name": request.form.get("platforms"),
            "all_ages": all_ages,
            "release_year": request.form.get("release_year"),
            "imdb": request.form.get("imdb"),
            "wtw": request.form.get("wtw"),
            "recommendation": request.form.get("recommendation"),
            "created_by": session["user"]
        }
        mongo.db.titles.insert_one(title)
        flash("Title Successfully Added")
        return redirect(url_for("add_title"))

    title_types = mongo.db.title_types.find().sort("title_name", 1)
    genres = mongo.db.genre.find().sort("genre_name", 1)
    platforms = mongo.db.platform.find().sort("platform_name", 1)
    return render_template(
        "add_title.html", title_types=title_types, genres=genres, platforms=platforms)


@app.route("/edit_title/<title_id>", methods=["GET", "POST"])
def edit_title(title_id):
    if request.method == "POST":
        all_ages = "yes" if request.form.get("all_ages") else "no"
        submit = {
            "title_name": request.form.get("title_name"),
            "type_name": request.form.get("title_types"),
            "genre_name": request.form.get("genres"),
            "platform_name": request.form.get("platforms"),
            "all_ages": all_ages,
            "release_year": request.form.get("release_year"),
            "imdb": request.form.get("imdb"),
            "wtw": request.form.get("wtw"),
            "recommendation": request.form.get("recommendation"),
            "created_by": session["user"]
        }
        mongo.db.titles.update({"_id": ObjectId(title_id)}, submit)
        flash("Title Successfully Updated")
        return redirect(url_for("get_titles"))

    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})

    title_types = mongo.db.title_types.find().sort("title_name", 1)
    genres = mongo.db.genre.find().sort("genre_name", 1)
    platforms = mongo.db.platform.find().sort("platform_name", 1)
    return render_template(
        "edit_title.html", title=title, title_types=title_types, genres=genres, platforms=platforms)


@app.route("/edit")
def edit():
    titles = list(mongo.db.titles.find())
    return render_template("edit.html", titles=titles)


@app.route("/logout")
def logout():
    flash("Logged out")
    session.pop("user")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
