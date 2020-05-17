from flask import Flask, render_template
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