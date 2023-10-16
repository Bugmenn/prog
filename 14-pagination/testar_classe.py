from config import *
from modelo import *

# exibindo todos os registros
#n = 1
#for c in db.session.query(Compania).all():
#    print(n, c.id, c.nome)
#    n+=1

# exibindo apenas 10 registros
n = 1        
for c in db.session.query(Compania).limit(10):
    print(n, c.id, c.nome)
    n+=1
# exibindo apenas registros entre 6 e 8
n = 1        
for c in db.session.query(Compania).offset(5).limit(3):
    print(n, c.id, c.nome)
    n+=1