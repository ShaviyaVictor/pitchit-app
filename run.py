# File that will run our application

from cProfile import run
from app import app, db



from app.models import user






@run.shell
def make_shell_context() :
  return dict(app = app, db = db, user = user)


if __name__ == '__main__' :
  app.run()