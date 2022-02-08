
from .. import db


# class User(db.Model) :
#   __tablename__ = 'users'
#   id = db.Column(db.Integer, primary_key = True)
#   username = db.Column(db.String(255))

# # The __repr__method is not really important. It makes it easier to debug our applications.
  
#   def __repr__(self) :
#       return f'User { self.username }'



class User(db.Model) :
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  firstName = db.Column(db.String(), nullable=False)
  lastName = db.Column(db.String(), nullable=False)
  username = db.Column(db.String(), nullable=False, unique=True)
  email = db.Column(db.String(), nullable=False)
  password = db.Column(db.String(), nullable=False)

  