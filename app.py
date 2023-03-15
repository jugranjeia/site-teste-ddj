from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
  return "Olá, mundo! Esse é meu site. (Julianna Granjeia)"

menu = """
<a href="/">Página inicial</a> | <a href="/textos">Textos</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def index():
  return menu + "Olá, mundo! Esse é meu site. (Julianna Granjeia)"

@app.route("/sobre")
def sobre():
  return menu + "Um site de teste da pós-graduação. Olha lá!"

@app.route("/contato")
def contato():
  return menu + "email@email.com"
