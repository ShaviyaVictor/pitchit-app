from app import db
from datetime import datetime


class Pitch(db.Model) :

  __tablename__ = 'pitches'

  id = db.Column(db.Integer, primary_key=True)
  pitches = db.Column(db.String(), nullable=False)
  createdAt = db.Column(db.DateTime(), default=datetime, nullable=False)