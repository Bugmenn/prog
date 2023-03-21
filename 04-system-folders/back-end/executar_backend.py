# importar os modelos
from modelo.pessoa import *

# importação das rotas
# exercício: converter a importação abaixo para funcionar "de uma só vez"
# algo assim: from rotas import *
# o que é preciso fazer?
from rotas import *

with app.app_context():
    CORS(app) # provendo o CORS ao sistema
   
    @app.route("/") # rota padrão
    def ola():
        return "backend operante"

    app.run(debug=True) # iniciar o servidor