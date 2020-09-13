from .db import db

class Music(db.Document):
    name = db.StringField(required=True, unique=True)
    albumtitle = db.ListField(db.StringField(), required=True)
    artist = db.ListField(db.StringField(), required=True)
        