from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
  return "Olá, mundo! Esse é meu site. (Julianna Granjeia)"

menu = """<p style="text-align: center; "><div style="background-color: black; border-radius: 5px; display: inline-block; padding: 10px;"><a href="/"><span style="color: rgb(255, 0, 0); font-family: &quot;Arial Black&quot;; font-size: 24px;">Página inicial</span></a> | <a href="/sobre"><span style="color: rgb(255, 0, 0); font-family: &quot;Arial Black&quot;; font-size: 24px;">Sobre</span></a> | <a href="/contato"><span style="color: rgb(255, 0, 0); font-family: &quot;Arial Black&quot;; font-size: 24px;">Contato</span></a></p></div><br>"""

@app.route("/")
def index():
  return menu + "Olá, mundo! Esse é meu site. (Julianna Granjeia)"

@app.route("/sobre")
def sobre():
  return menu + "Um site de teste da pós-graduação. Olha lá!"

@app.route("/contato")
def contato():
  return menu + "email@email.com"
