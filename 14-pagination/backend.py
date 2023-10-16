from config import *
from modelo import *

@app.route("/listar/<string:classe>")
def listar(classe):
    # obter os dados da classe informada
    dados = None
    if classe == "Compania":
        dados = db.session.query(Compania).all()
    if dados:
      # converter dados para json
      lista_jsons = [x.json() for x in dados]

      meujson = {"resultado": "ok"}
      meujson.update({"detalhes": lista_jsons})
      return jsonify(meujson)
    else:
      return jsonify({"resultado":"erro", "detalhes":"classe informada inválida: "+classe})
    
@app.route("/listar_paginado/<string:classe>/<int:pagina>")
def listar_paginado(classe, pagina):
    # obter os dados da classe informada
    dados = None
    if classe == "Compania":
        # retornar resultados a partir de uma página, com número limitado de resultados por página
        dados = db.session.query(Compania).paginate(page=pagina, per_page=1000)
    if dados:
      # converter dados para json
      lista_jsons = [x.json() for x in dados]

      meujson = {"resultado": "ok"}
      meujson.update({"detalhes": lista_jsons})
      return jsonify(meujson)
    else:
      return jsonify({"resultado":"erro", "detalhes":"classe informada inválida: "+classe})    

# rota padrão
@app.route("/")
def inicio():
    return 'backend ok'

app.run(debug=True)