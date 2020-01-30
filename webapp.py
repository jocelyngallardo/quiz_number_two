Learn more or give us feedback
import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #SECRET_KEY is an environment variable.  
                                         #The value should be set in Heroku (Settings->Config Vars).  
results = {"answer1":"", "answer2":""}
answers = {"answer1":"1", "answer2":"3"}

@app.route('/')
def renderMain():
    return render_template('home.html')

#@app.route('/startOver')
#def startOver():
    #TODO: delete everything from the session
    
    return redirect('/')

@app.route('/page1',methods=['GET','POST'])
def renderPage1():
    #TODO: sale the first and last name in the session
    session["answer1"] = request.form["question1"]
    results["answer1"] = session["answer1"]
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    #TODO: save the favorite color in the session
    session["answer2"] = request.form["question2"]
    results["answer2"] = session["answer2"]
    return render_template('page2.html')
  
@app.route('/page3',methods=['GET','POST'])
def renderPage3():
  response = ""
  for key in results:
    if results[key] == answer[key]:
      response += "Correct! You're a wizard, Harry."
    else:
      response += "You chose" + results[key] + ". The correct answer is: " + answer[key] + "."
    return render_template('page3.html', response = response)
    
if __name__=="__main__":
    app.run(debug=False)

