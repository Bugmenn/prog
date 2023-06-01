from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# configurações
app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'animais.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    raca = db.Column(db.String(254))
    cor = db.Column(db.String(254))
    genero = db.Column(db.String(254))

    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity':'animal', 
        'polymorphic_on':type
    }

    def __str__(self):
        return f'{self.nome}, {self.raca}, {self.cor}, {self.genero}'

class Gato(Animal):
    id = db.Column(db.Integer, db.ForeignKey('animal.id'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity':'gato',
    }

    fugas = db.Column(db.Integer)

    def __str__(self):
        return super().__str__() + f', fugas={self.fugas}'

class Cachorro(Animal):
    id = db.Column(db.Integer, db.ForeignKey('animal.id'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity':'cachorro'
    }

    def __str__(self):
        return super().__str__()

with app.app_context():

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    merlin = Gato(nome = 'Merlin', raca = 'persa', cor = 'preto', genero = 'Masculino', fugas = 4)         
    print(f'Gato: {merlin}')

    db.session.add(merlin)
    db.session.commit()

    bilu = Cachorro(nome = 'Bilu', raca = 'buldog', cor = 'marrom', genero = 'Masculino')
    print(f'Cachorro: {bilu}')
    db.session.add(bilu)
    db.session.commit()

    print("Listando animais:")
    for p in db.session.query(Animal).all():
        print(p)