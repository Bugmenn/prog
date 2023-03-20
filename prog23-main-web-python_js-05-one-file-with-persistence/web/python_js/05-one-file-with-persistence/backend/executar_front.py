from config.config import *

with app.app_context():

    @app.route("/")
    def ola():
        return "backend operante"

    # criar o banco de dados, caso não esteja criado
    db.create_all()

    # provendo o CORS ao sistema
    CORS(app)

    # iniciar o servidor
    app.run(debug=True)