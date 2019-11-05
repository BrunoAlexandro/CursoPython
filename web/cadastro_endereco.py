class Endereco:

    logradouro = ''
    numero = ''
    bairro = ''
    cidade = ''
    cep = ''

    #É obrigatorio criar uma variável para retornar algo do return.
    def endereco(self):
        self.logradouro = input('Digite sua rua: ')
        self.numero = input('Digite o número: ')
        self.bairro = input('Digite o bairro: ')
        self.cidade = input('Digite a cidade: ')
        self.cep = input('Digite o CEP: ')
        return f'Seu logradouro é: {self.logradouro}\n Seu número é {self.numero}\n Seu bairro é: {self.bairro}\n Sua cidade é: {self.cidade}\n Seu CEP é: {self.cep}\n '
    #SEGUNDA OPÇÃO
    # usuario = f'Nome: {nome}\n sobrenome: {sobrenome}\n data nascimento: {data_nascimento}\n email {email}\n senha {senha}\n'
    # return usuario