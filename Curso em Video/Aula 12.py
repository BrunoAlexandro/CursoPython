nome = str(input('Digite um nome: '))

if nome == 'Bruno':
    print(f'Que nome bonito.')
elif nome == 'Pedro' or nome =='Calor' or nome == 'Paulo':
    print('Seu nome é bem popular.')
elif nome in 'Joice Vargas de Lima':
    print('Que belo nome Feminino.') #In é usado para pegar uma palavra de dentro do contexto.
else:
    print(f'Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}')
