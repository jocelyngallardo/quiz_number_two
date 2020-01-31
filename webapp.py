import os
from flask import Flask, url_for, render_template, request, Markup
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #SECRET_KEY is an environment variable.  
                                         #The value should be set in Heroku (Settings->Config Vars).  
answers = {"answer1":"Feet", "answer2":"Blue", "answer3":"Bats"}

@app.route('/', methods=['GET','POST'])
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear()
    return redirect('/')

@app.route('/page1',methods=['GET','POST'])
def renderPage1():
    #TODO: sale the first and last name in the session
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    #TODO: save the favorite color in the session
    if not "answer1" in session:
      session["answer1"] = request.form["question1"]
    else:
      session["answer1"] != request.form["question1"]
    return render_template('page2.html')
  
 @app.route('/page3',methods=['GET','POST'])
 def renderPage3():
    #TODO: save the favorite color in the session
    if not "answer2" in session:
      session["answer2"] = request.form["question2"]
    else:
      session["answer2"] != request.form["question2"]
    return render_template('page3.html')
  
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
  if not "answer3" in session:
    session["answer3"] = request.form["question3"]
  else:
    session["answer3"] != request.form["question3"]
    
  response = ""
  for key in session:
    if session[key] == answers[key]:
      response += Markup("<li>" + "Correct! You're a wizard, Harry." + "</li>")
    else:
      response += Markup("<li>" + "You chose: " + session[key] + ". The correct answer is: " + answers[key] + "." + "</li>")
  return render_template('page4.html', response = response)
    
if __name__=="__main__":
    app.run(debug=False)

