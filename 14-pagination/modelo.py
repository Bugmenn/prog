from config import *

# n,name,domain,year founded,industry,
# size range,locality,country,linkedin url,
# current employee estimate,
# total employee estimate

class Compania(db.Model):
    # atributos da pessoa
    id = db.Column('n', db.Integer, primary_key=True)
    nome = db.Column('name',db.String(254))
    dominio = db.Column('domain',db.String(254))
    ano = db.Column('year founded', db.String(254))
    industria = db.Column('industry',db.String(254))
    tamanho = db.Column('size range', db.String(254))
    localizacao = db.Column('locality', db.String(254))
    pais = db.Column('country', db.String(254))
    linkedin = db.Column('linkedin url', db.String(254))
    empregados_atual = db.Column('current employee estimate', db.String(254))
    empregados_total = db.Column('total employee estimate', db.String(254))

    def json(self):
        return {
            'id' : self.id,
            'nome' : self.nome,
            'dominio' : self.dominio,
            'ano' : self.ano, 
            'industria' : self.industria, 
            'tamanho' : self.tamanho,
            'localizacao' : self.localizacao,
            'pais' : self.pais,
            'linkedin' : self.linkedin,
            'empregados_atual' : self.empregados_atual,
            'empregados_total' : self.empregados_total
        }