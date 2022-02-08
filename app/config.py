class Config :
  '''
  General configuration parent class
  '''
  pass
  # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:Access@localhost/pitchit'



class ProdConfig(Config) :
  '''
  Production  configuration child class

  Args:
    Config: The parent configuration class with General configuration settings
  '''
  pass



class DevConfig(Config) :
  '''
  Development  configuration child class

  Args:
    Config: The parent configuration class with General configuration settings
  '''
  
  DEBUG = True