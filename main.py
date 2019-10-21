from flask import Flask,request,render_template, jsonify
from multiprocessing import Value
import random


app = Flask(__name__)



@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ruleta',methods=['POST', 'GET'])
def ruleta():
  if request.method == 'POST':

    bonuses = request.form
    fijos = ['1000€', 'Perder', 'mitad_dinero', '500€', '200€', '-turno-1000€']
    tirada = random.choice(fijos)
    if tirada == 'Perder':
      return render_template("perder.html", tirada=tirada)
    
    with open('tiradas.txt', 'a+') as f:
      f.write(tirada + '\n')
      f.close()
    historial = open('tiradas.txt', 'r')
    r_historial = historial.read()
    
  return render_template("ruleta.html", bonuses=bonuses, fijos=fijos, fijo=tirada, historial=r_historial)

# def perder(tirada):
#   if tirada == 'Perder':
#     return render_template("perder.html", tirada=tirada)

if __name__ == "__main__":
    app.run(debug=True)