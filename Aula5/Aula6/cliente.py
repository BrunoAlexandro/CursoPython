class Cliente:
    
    def __init__(self, nome, cpf, data_nascimento, id=None):
        self.id = id
        self.nome = nome
        self.CPF = cpf
        self.data_nascimento = data_nascimento

