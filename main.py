from flask import Flask, render_template
from data import db_session
from data.users import User
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

for job in db_sees.query(Jobs).all():
    team_leader = db_sees.query(User).filter(User.id == job.team_leader).first()
    team_leader_name = f"{team_leader.surname} {team_leader.name}"
    data.append([job.id, job.job, team_leader_name, job.work_size, job.collaborators, is_finished(job.is_finished)])

@app.route("/")
def start():
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")