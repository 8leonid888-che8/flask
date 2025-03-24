import sqlalchemy
from .db_session import SqlAlchemyBase

class Department(SqlAlchemyBase):
    ___tablename__ = "departments"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief =  sqlalchemy.Column(sqlalchemy.Integer)
    members = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)