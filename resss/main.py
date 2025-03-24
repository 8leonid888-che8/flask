from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/table/<gender>/<age>")
def menu(gender, age):
    return render_template("index.html",  gender=gender, age=age)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
