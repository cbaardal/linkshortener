from app import db

class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longurl = db.Column(db.String(1024), index=True, unique=True)
    shorturl = db.Column(db.String(24), index=True, unique=True)

    def __repr__(self):
        return '{}'.format(self.longurl)
