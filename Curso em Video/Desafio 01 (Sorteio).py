from random import randint

# Faça o usuario acertar o numero entre 0 e 5 que o computador escolheu randomicamente
print('=-'*20)
print('Vou pensar em um número entre 0 e 5')
print('=-'*20)

jogador = int(input('Em que numero pensei? '))
computador = randint(0, 5) #Faz o computador sortear


if jogador == computador:
    print(f'Parabéns você ganhou, pensou no número {jogador}')
else:
    print(f'Você perdeu, o computador pensou no número {computador}.')


