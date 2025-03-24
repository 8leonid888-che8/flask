from datetime import datetime

from data import db_session
from data.db_session import global_init, create_session

db_session.global_init("db/blogs.db")
import datetime
from collections import defaultdict


name = input()


global_init(name)
db_sess = create_session()

for i in db_sess.query(User).filter(User.address == "module_1", User.age < 21).all():
    i.address = "module_3"
    db_sess.commit()