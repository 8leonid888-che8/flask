from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def menu():
    return "<b>Миссия Колонизация Марса</b>"


@app.route("/index")
def index():
    return "<b>И на Марсе будут яблони цвести!</b>"


@app.route('/promotion')
def countdown():
    countdown_list = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                      "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(map(lambda x: f"<b>{x}</b>", countdown_list))


@app.route("/image_mars")
def image_mars():
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <title>Привет, Яндекс!</title>
  <meta charset="UTF-8">
</head>
<body>
<h1>
  <b>Жди нас, Марс!</b>
</h1>
<img src="{url_for('static', filename='img/image_mars.png')}" alt="здесь должна была быть картинка, но не нашлась">
<p>Вот она какая, красная планета.</p>  
</body>
</html>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
