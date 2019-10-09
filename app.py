from flask import Flask,request,render_template,jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process',methods= ['POST'])
def process():
    numero1  = float(request.form['numero1'])
    numero2 = float(request.form['numero2'])
    operador = request.form['operador']
    if operador == '+':   
        output = numero1 + numero2
        return jsonify({'output': + output})       
    elif operador == '-':
        output = numero1 - numero2
        return jsonify({'output': + output})
    elif operador == '*':
        output = numero1 * numero2
        return jsonify({'output': + output})
    elif operador == '/':
        output = numero1 / numero2
        return jsonify({'output': + output})
    else :
         return 'nop'