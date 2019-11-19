from flask_mysqldb import MySQLdb
from cliente import Cliente

class ClienteDao:

    def lista_todos(self):
        conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database='zuplae04')
        cursor = conexao.cursor()
        cursor.execute('SELECT  NOME, CPF, DATA_NASCIMENTO, ID FROM Cliente')#'SELECT * FROM é para pegar os dados de uma certa tabela
        lista_resultado = cursor.fetchall()
        lista_clientes = []
        for c in lista_resultado:
            cliente = Cliente(c[0], c[1], c[2], c[3])
            lista_clientes.append(cliente)
            #print(c.__dict__) #Dict converte uma tupla em dicionário.
        return lista_clientes
        
    
    def buscar_por_id(self, id:int):
        conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database='zuplae04')
        cursor = conexao.cursor()
        cursor.execute(f'SELECT  NOME, CPF, DATA_NASCIMENTO, ID FROM Cliente WHERE ID = {id}')
        c = cursor.fetchone()#fatone serve para pegar apenas um.
        cliente = Cliente(c[0], c[1], c[2], c[3])
        return cliente

    def salvar(self, cliente:Cliente):
        conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database='zuplae04')
        cursor = conexao.cursor()
        cursor.execute(f'INSERT INTO Cliente ( NOME, CPF, DATA_NASCIMENTO ) VALUES( "{cliente.nome}", "{cliente.cpf}", "{cliente.data_nascimento}" )')
        conexao.commit()
        conexao.close()
    def alterar(self, cliente:Cliente):
        conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database='zuplae04')
        cursor = conexao.cursor()
        cursor.execute('UPDATE Client set nome="{cliente.nome}", cpf="{cliente.cpf}", data_nascimento="{cliente.data_nascimento}", id="{cliente.id}"')
        conexao.commit()
        conexao.close()
    def deletar(self, id:int ):
        conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database='zuplae04')
        cursor = conexao.cursor()
        cursor.execute(f'DELETE FROM Cliente WHERE ID = {id}')
        conexao.commit()
        conexao.close()