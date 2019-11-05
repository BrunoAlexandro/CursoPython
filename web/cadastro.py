from cadastro_usuario import Pessoa
from cadastro_endereco import Endereco

print('='*50)
print('\n'*2)

#Para dar um print de um método dentro de uma classe é necessário sempre criar uma variável da classe, EX:

usuario = Pessoa()
endereco = Endereco()


print(usuario.cadastrar_usuario())
print(endereco.endereco())

#OU para printar algo específico na função
#print(usuario.nome)
#print(endereco.logradouro)


print('\n'*2)

