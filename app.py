from flask import Flask, render_template, request, flash, redirect, url_for, abort
from jinja2 import environment
import csv
app = Flask(__name__)

app.config["SECRET_KEY"] = "secretkey"

##########
# Tutorial #1
##########

@app.route("/")
def index():
    return "Hello, World!"


@app.route("/html")
def html():
    return render_template("index.html")


##########
# Tutorial #2
##########

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/hello/<string:name>")
def hello_myname(name):
    return render_template("hello.html", name=name)

##########
# Tutorial #3
##########

def dateformat(value, format="%m-%d-%Y"):
    return value.strftime(format)

app.jinja_env.filters["dateformat"] = dateformat

@app.route("/jinja")
def jinja_demo():
    import datetime
    name = "DevWithMe"
    num = 0
    numbers = [1, 2, 3, 4, 5, 6]
    fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}
    return render_template("jinja.html", name=name, num=num, numbers=numbers, fruits=fruits, date=datetime.datetime.now())


######
# Tutorial #4
######

# GET POST

@app.route("/forms", methods=["GET", "POST"])
def forms():
    if request.method == "POST":
        with open("user.csv", "a") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["username", "password"])
            writer.writerow({"username": request.form.get("username"), "password": request.form.get("password")})
        return "success"

    if request.args.get("username"):
        return str(request.args.get("username"))

    return render_template("forms.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        with open("user.csv", "r") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                if row[0] == request.form.get("username") and row[1] == request.form.get("password"):
                    return "you're logged in!"
            flash("Wrong Credentials", category="danger")
            return redirect(url_for("index"))
    else:
        return render_template("forms.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        with open("user.csv", "a") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["username", "password"])
            writer.writerow({"username": request.form.get("username"), "password": request.form.get("password")})
        return "successfully registered"
    else:
        return render_template("forms.html")

######
# Tutorial #4
######

import sqlite3

conn = sqlite3.connect("example.sqlite3", check_same_thread=False)
c = conn.cursor()

######
# Tutorial #23(?)
######

@app.route("/adminonly")
def adminonly():
    return [0, 1, 2, 3][70]
    # abort(403)

@app.errorhandler(IndexError)
def no_permission(e):
    return "You don't have permission to view this page", 403