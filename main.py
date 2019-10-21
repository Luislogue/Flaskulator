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
    with open('tiradas.txt', 'a+') as f:
      f.write(tirada + '\n')
      f.close()
    return render_template("ruleta.html", bonuses=bonuses, fijos=fijos, fijo=tirada)


if __name__ == "__main__":
    app.run(debug=True)