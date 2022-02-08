from flask import Flask
from .config import DevConfig
# from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


# from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__)

db = SQLAlchemy(app)

# db = SQLAlchemy()

# Setting up configuration
app.config.from_object(DevConfig)


# Initializing Flask Extensions
# bootstrap = Bootstrap(app)
# db.init_app(app)


from app import views