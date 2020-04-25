import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Topic(SqlAlchemyBase):
    __tablename__ = 'topics'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    topic_title = sqlalchemy.Column(sqlalchemy.String)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
    site = orm.relation("Site", back_populates='topic')

    def __repr__(self):
        return f'<Topic> {str(self.id) }, {self.topic_title}'
