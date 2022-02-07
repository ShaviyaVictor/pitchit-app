from flask import render_template
from app import app



# views
@app.route('/')
def index() :
  '''
  View root page function that returns the index page and its data
  '''
  return render_template('index.html')



@app.route('/pitches')
def pitch() :
  '''
  View pitch page function that returns the pitches available
  '''