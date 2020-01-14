import datetime
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


# @app.route("/")
# def index():
#     return "Hello World Welcome to the table of men"


@app.route("/david")
def david():
    headline = "Hello World"
    return render_template("index.html", headline=headline)


@app.route("/<string:names>")
def name(names):
    names = names.capitalize()
    return f"Welcome to the new world {names}"


@app.route("/christmas")
def christmas():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template(new_year=new_year)


@app.route("/array")
def array():
    names = ["Kojo", "Frank", "Kobina"]
    return render_template("index.html", names=names)


@app.route('/contactus')
def contactus():
    return render_template("contactus.html")


@app.route('/')
def index():
    return render_template("index.html")
