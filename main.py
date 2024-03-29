from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def home():
    return render_template("home.html")


@application.route("/about/")
def about():
    return render_template("about.html")


@application.route("/characters/")
def characters():
    return render_template("about.html")


@application.route("/download/")
def download():
    return render_template("download.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0')
