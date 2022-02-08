import secrets
import os



class Base :
  Flask_APP='run.py'
  SQLALCHEMY_TRACK_MODIFICATION = False
  SECRET_KEY = secrets.token_hex(16)



class Development(Base) :
  FLASK_ENV = 'development'
  DATABASE = ''
  POSTGRES_USER = ''
  POSTGRES_PASSWORD = ''
  SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/pitchit.db'



class Staging(Base) :
  DATABASE = ''
  POSTGRES_USER = ''
  POSTGRES_PASSWORD = ''
  SQLALCHEMY_DATABASE_URI = ''



class Production(Base) :
  DATABASE = ''
  POSTGRES_USER = ''
  POSTGRES_PASSWORD = ''
  SQLALCHEMY_DATABASE_URI = ''