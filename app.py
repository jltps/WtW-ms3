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


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    titles = list(mongo.db.titles.find({"$text": {"$search": query}}))
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

        mongo.db.titles.drop_indexes()
        mongo.db.titles.create_index([("title_name", "text"), ("genre_name", "text"), (
            "type_name", "text"), ("platform_name", "text"), ("release_year", "text"), ("created_by", "text")])
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

        mongo.db.titles.drop_indexes()
        mongo.db.titles.create_index([("title_name", "text"), ("genre_name", "text"), (
            "type_name", "text"), ("platform_name", "text"), ("release_year", "text"), ("created_by", "text")])
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


@app.route("/delete_title/<title_id>")
def delete_title(title_id):
    mongo.db.titles.remove({"_id": ObjectId(title_id)})
    flash("Title Successfully Deleted")

    mongo.db.titles.drop_indexes()
    mongo.db.titles.create_index([("title_name", "text"), ("genre_name", "text"), (
        "type_name", "text"), ("platform_name", "text"), ("release_year", "text"), ("created_by", "text")])
    return redirect(url_for("get_titles"))


@app.route("/manage")
def manage():
    return render_template("manage.html")


@app.route("/manage_types")
def manage_types():
    types = list(mongo.db.title_types.find().sort("type_name", 1))
    return render_template("manage_types.html", types=types)


@app.route("/add_type", methods=["GET", "POST"])
def add_type():
    if request.method == "POST":
        new_type = {
            "type_name": request.form.get("type_name")
        }
        mongo.db.title_types.insert_one(new_type)
        flash("New Type successfully added")
        return redirect(url_for("manage_types"))

    return render_template("add_type.html")


@app.route("/edit_type/<type_id>", methods=["GET", "POST"])
def edit_type(type_id):
    if request.method == "POST":
        new_type = {
            "type_name": request.form.get("type_name")
        }
        mongo.db.title_types.update(
            {"_id": ObjectId(type_id)}, new_type)
        flash("Type Successfully Updated")
        return redirect(url_for("manage_types"))

    this_type = mongo.db.title_types.find_one({"_id": ObjectId(type_id)})
    return render_template("edit_type.html", type_id=this_type)


@app.route("/delete_type/<type_id>")
def delete_type(type_id):
    mongo.db.title_types.remove({"_id": ObjectId(type_id)})
    flash("Type Successfully Deleted")
    return redirect(url_for("manage_types"))


@app.route("/manage_genres")
def manage_genres():
    genres = list(mongo.db.genre.find().sort("genre_name", 1))
    return render_template("manage_genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        new_genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genre.insert_one(new_genre)
        flash("New Genre successfully added")
        return redirect(url_for("manage_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        new_genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genre.update(
            {"_id": ObjectId(genre_id)}, new_genre)
        flash("Genre Successfully Updated")
        return redirect(url_for("manage_genres"))

    this_genre = mongo.db.genre.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre_id=this_genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genre.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("manage_genres"))


@app.route("/manage_platforms")
def manage_platforms():
    platforms = list(mongo.db.platform.find().sort("platform_name", 1))
    return render_template("manage_platforms.html", platforms=platforms)


@app.route("/add_platform", methods=["GET", "POST"])
def add_platform():
    if request.method == "POST":
        new_platform = {
            "platform_name": request.form.get("platform_name")
        }
        mongo.db.platform.insert_one(new_platform)
        flash("New Platform successfully added")
        return redirect(url_for("manage_platforms"))

    return render_template("add_platform.html")


@app.route("/edit_platform/<platform_id>", methods=["GET", "POST"])
def edit_platform(platform_id):
    if request.method == "POST":
        new_platform = {
            "platform_name": request.form.get("platform_name")
        }
        mongo.db.platform.update(
            {"_id": ObjectId(platform_id)}, new_platform)
        flash("Platform Successfully Updated")
        return redirect(url_for("manage_platforms"))

    this_platform = mongo.db.platform.find_one({"_id": ObjectId(platform_id)})
    return render_template("edit_platform.html", platform_id=this_platform)


@app.route("/delete_platform/<platform_id>")
def delete_platform(platform_id):
    mongo.db.platform.remove({"_id": ObjectId(platform_id)})
    flash("Platform Successfully Deleted")
    return redirect(url_for("manage_platforms"))


@app.route("/logout")
def logout():
    flash("Logged out")
    session.pop("user")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
