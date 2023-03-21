from config.configuracoes import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    email = db.Column(db.Text)
    telefone = db.Column(db.Text)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'(id={self.id}) {self.nome}, ' +\
            f'{self.email}, {self.telefone}'

    # expressar a classe em formato json
    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }