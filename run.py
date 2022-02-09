# File that will run our application

# from cProfile import run
# from multiprocessing import Manager
# from flask_script import Manager
from app import app


# from flask import Flask


# manager = Manager(app)


# from app.models import user

# app = Flask(__name__)



# a Python shell that allows us to pass in some properties into our shell
# @manager.shell
# def make_shell_context() :
#   return dict(app = app, db = db, user = user)


if __name__ == '__main__' :
  app.run(debug = True)