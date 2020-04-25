import sqlalchemy
from sqlalchemy import orm
import datetime

from .db_session import SqlAlchemyBase

class Site(SqlAlchemyBase):
    __tablename__ = 'sites'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    site_address = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    site_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    id_topic = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("topics.id"))
    date_added = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    site_description = sqlalchemy.Column(sqlalchemy.String)
    topic = orm.relation('Topic')
    user = orm.relation('User')

    def __repr__(self):
        return f'<Site> URL {self.site_address} - {self.site_name}'
