import datetime as dt

class User():
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self) -> str:
        return '<User(name={self.name!r})>'.format(self=self)
