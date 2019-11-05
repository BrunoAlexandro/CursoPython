#CRIAR UMA LISTA
alunos = ['Maykon', 'Cris', 'Jr', 'Nikolas', 'Rafael', 'BrunoB','BrunoS' ]

#FOR É PARA REPETIR OU LER ALGO

#Para usar um determinado valor dentro da variável alunos.    
# for i in range(0,6):
#     print(alunos[i])

# for i in range(0,3):
#     print('Ola')


#Atribui tudo o que há dentro de alunos para o valor i.
print('Primeira execução: ')
for i in alunos:
    print(i)
    alunos.append('Append adiciona algo a lista') #Append serve para adicionar algo na lista.
    print(alunos.count('Bruno')) #count serve para adicionar contar quantos intens tem em cada lista.
