from flask import render_template
from app import app
# from .forms import logInForm, signUpForm, pitchForm



# views
@app.route('/')
def index() :
  '''
  View root page function that returns the index page and its data
  '''

  title = 'Pitch It'

  return render_template('index.html', title = title)



@app.route('/pitches')
def pitch() :
  '''
  View pitch page function that returns the pitches available
  '''

  title = 'Pitches'

  return render_template('pitch.html', title = title)



@app.route('/login')
def login() :
  '''
  View login page function that opens the login form
  '''

  # form = logInForm()

  title = 'Pitch it | login'

  return render_template('login.html', title = title)



@app.route('/register')
def register() :
  '''
  View registration page function that opens the registration form
  '''

  # form = signUpForm()

  title = 'Pitch it | sign up'

  return render_template('signup.html', title = title)



@app.route('/logout')
def logout() :
  '''
  View logout page function that logs a user out
  '''


  title = 'Pitch it | logout'

  return render_template('logout.html', title = title)