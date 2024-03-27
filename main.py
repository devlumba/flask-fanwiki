from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def hello_world():
    return render_template("base.html")


@application.route("/about")
def about():
    return render_template("about.html", title="About")


@application.route("/characters")
def characters():
    pass


@application.route("/staff")
def staff():
    pass


if __name__ == "__main__":
    application.run(host='0.0.0.0')