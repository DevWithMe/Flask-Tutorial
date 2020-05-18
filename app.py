from flask import Flask, render_template
from jinja2 import environment
app = Flask(__name__)



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