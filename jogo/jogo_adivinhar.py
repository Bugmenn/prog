import random
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'jogo.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    tentativas = db.Column(db.Integer)
    numero_para_acertar = db.Column(db.Integer)

# tentativas que o jogador leva para acertar
tentativas_jogador = 0

numero = random.randint(1,10) #numero gerado aleatoriamente entre 1 e 10 (incluindo eles)

nome = str(input('Informe seu nome:'))

print('O número está entre 1 e 10!')

while True:
    resposta = int(input('Escolha o número:'))

    if resposta < 1 or resposta > 10:
        print('O número deve ser entre 1 e 10!')
        continue

    elif resposta < numero:
        print('Está abaixo do número')
        tentativas_jogador += 1

    
    elif resposta > numero:
        print('Está acima do número')
        tentativas_jogador += 1
    
    elif resposta == numero:
        print('\nVocê ganhou!!!!',f'\nO número era {numero}',f'\nLevou {tentativas_jogador} tentativas')
        break

with app.app_context():

    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    
    db.create_all()

    jogador = Jogador(nome=nome, tentativas=tentativas_jogador, numero_para_acertar=numero)         
    print(f'Jogador: {jogador}')
    db.session.add(jogador)
    db.session.commit()

    print("Listando animais:")
    for p in db.session.query(Jogador).all():
        print(p)