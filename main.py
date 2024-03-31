import werkzeug.exceptions
from flask import Flask, render_template

application = Flask(__name__)
application.config['TRAP_HTTP_EXCEPTIONS']=True


@application.route("/")
def home():
    return render_template("home.html")


@application.route("/about/")
def about():
    return render_template("about.html", title="Новелла")


@application.route("/characters/")
def characters():
    return render_template("characters.html", title="Персонажи")


@application.route("/download/")
def download():
    return render_template("download.html", title="Скачать")


@application.route("/creators/")
def staff():
    return render_template("staff.html", title='Создатели')


@application.errorhandler(Exception)
def bad_request(e):
    try:
        if e.code == 404:
            return render_template("404.html", title="Ошибка 404!"), 404
    except:
        pass


if __name__ == "__main__":
    application.run(host='0.0.0.0')
