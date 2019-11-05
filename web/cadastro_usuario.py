# Não necessita de parênteses ao inciar, Ex: class Pessoa():
class Pessoa:
  
  nome = ''
  sobrenome = ''
  data_nascimento = ''
  email = ''
  senha = ''

#É obrigatorio criar uma variável para retornar algo do return.
  #Sempre que tiver um método dentro de uma classe, então SEMPRE por o self dentro do método.
  def cadastrar_usuario(self):
          self.nome = input('Digite seu nome:')
          self.sobrenome = input('Digite seu sobrenome:')
          self.data_nascimento = (input('Digite sua data de nascimento: '))
          self.email = input('Digite seu e-mail: ')
          self.senha = input('Digite sua senha: ')
          return f'Nome: {self.nome}\n sobrenome: {self.sobrenome}\n data nascimento: {self.data_nascimento}\n email {self.email}\n senha {self.senha}\n'

  def busca_endereco(self):
    return self
  #SEGUNDA OPÇÃO
   # usuario = f'Nome: {nome}\n sobrenome: {sobrenome}\n data nascimento: {data_nascimento}\n email {email}\n senha {senha}\n'
   # return cadastrar_usuario




