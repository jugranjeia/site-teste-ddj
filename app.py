from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
  return "Olá, mundo! Esse é meu site. (Julianna Granjeia)"

@app.route("/sobre")
def sobre():
  return "Testando. Que coisa!"

@app.route("/contato")
def contato():
  return "judinanina@gmail.com"
