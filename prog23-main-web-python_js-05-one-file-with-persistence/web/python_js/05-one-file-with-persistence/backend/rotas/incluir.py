from config.config import *
from modelo.class_pessoa import *

# curl localhost:5000/incluir_pessoa -X POST -d '{"nome":"john", "email":"jo@gmail.com", "telefone":"91234567"}' -H "Content-Type:application/json"
@app.route("/incluir_pessoa", methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        # cria a pessoa
        nova = Pessoa(**dados)
        # realiza a persistência da nova pessoa
        db.session.add(nova)
        db.session.commit()
        # tudo certo :-) resposta de sucesso
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:
        # informar mensagem de erro
        return jsonify({"resultado": "erro", "detalhes": str(e)})