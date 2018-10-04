from app import db


class User(db.Model):

    __tablename__ = 'tb_users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(125), unique=True)
    email = db.Column(db.String(125), unique=True)
    _password = db.Column(db.String(50))
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f'User(first_name="{self.first_name}", last_name="{self.last_name}", username="{self.username}", email="{self.email}", _password={self._password})'

    def __str__(self):
        return f'({self.username}) - {self.email}'

    def as_dict(self):
        return {u.name: getattr(self, u.name) for u in self.__table__.columns}
