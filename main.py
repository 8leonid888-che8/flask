from flask import Flask, render_template
from data import db_session
from data.db_session import global_init, create_session
from data.jobs import Jobs


app = Flask(__name__)
db_session.global_init("db/blogs.db")
db_sees = db_session.create_session()
data = []
def is_finished(f):
    if f:
        return "is finished"
    else:
        return "is not finished"

for i in db_sees.query(Jobs).all():
    data.append([i.id, i.job, i.team_leader, i.work_size, i.collaborators, is_finished(i.is_finished)])

@app.route("/")
def start():
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")