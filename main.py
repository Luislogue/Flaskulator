from flask import Flask,request,render_template, session, url_for,redirect
from flask_wtf import FlaskForm, Form
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


import random


app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'



@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ruleta',methods=['POST', 'GET'])
def ruleta():
  if request.method == 'POST':
    
    bonuses = request.form.getlist('check')
    session['bonus'] = bonuses
    # bonus = session['bonus']
    
    fijos = ['1000€', 'Perder', 'mitad dinero', '500€', '200€', '-1 turno y-1000€']
    tirada = random.choice(fijos)
    if tirada == 'Perder':
      
      f = open('tiradas.txt', 'r+')
      f.truncate(0)
      session['visits'] = 0
      return render_template("perder.html", tirada=tirada)
    
    with open('tiradas.txt', 'a+') as f:
      f.write(tirada + '\n')
      f.close()
    historial = open('tiradas.txt', 'r')
    r_historial = historial.read()

    if 'visits' in session:
      session['visits'] = session.get('visits') + 1
  
    else:
      session['visits'] = 1 
    tiradas = session['visits'] 

    if tirada == '-1 turno y-1000€':
      
      tiradas = tiradas + 1
      
 
  return render_template("ruleta.html", bonuses=session['bonus'], fijos=fijos, fijo=tirada, historial=r_historial, tiradas=tiradas)

@app.route('/ganar', methods=['POST','GET'])
def ganar():

  historial = open('tiradas.txt', 'r')
  r_historial = historial.read()
  return render_template("ganar.html", historial=r_historial)


if __name__ == "__main__":
    app.run(debug=True)