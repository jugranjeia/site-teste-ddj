from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
  return "Olá, mundo! Esse é meu site. (Julianna Granjeia)"

menu="""
<a href="/">Página inicial</a> | <a href="/sobre">Sobre</a> ! <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def hello_world():
  return menu+"Olá, mundo! Esse é o meu site. (Julianna Granjeia)"

@app.route("/sobre")
def sobre():
  return menu+"Aqui vai o conteúdo da página Sobre"

@app.route("/contato")
def contato():
  return menu+"Aqui vai o conteúdo da página Contato"
