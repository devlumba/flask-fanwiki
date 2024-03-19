from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("base.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/characters")
def characters():
    pass


@app.route("/персонажи")
def characters_ru():
    return "Персонажи"


@app.route("/staff")
def staff():
    pass
