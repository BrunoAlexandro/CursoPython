from cliente_dao import ClienteDao
from cliente import Cliente

cliente_novo = Cliente('Bruno','054.655.243-65','1970-08-15', )

dao = ClienteDao()
#dao.salvar(cliente_novo)

#print(dao.buscar_por_id(10).__dict__)

for cliente in dao.lista_todos():
    print(cliente.__dict__)