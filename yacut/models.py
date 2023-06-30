from datetime import datetime as dt

from flask import url_for

from . import db, views


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=dt.utcnow)

    def from_dict(self, data):
        self.original = data["url"]
        self.short = data["custom_id"]

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for("redirect_view", short=self.short, _external=True),
        )
