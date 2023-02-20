from flask import Flask

app = Flask(__name__)

@app.route("/")
def primario():
    return """<b>Site teste de <u>Gabriel Bugmann</u></b><br>
    <b><i>301 - Info</i></b>
    <a href="/lista_pessoas">Link</a>"""

@app.route("/lista_pessoas")
def lista_pessoas():
    lista = ["João da Silva","Maria Oliveira"]
    for i in lista:
        return f'<p>{i}</p>'

app.run(debug=True, host="0.0.0.0")