velocidade = int(input('Digite a velocidade do carro: '))
resultado = (velocidade-80)*7

if velocidade >= 80:
    print(f'Você foi multado em {resultado} reais.')
else:
    print('Você não será multado. Boa viagem.')

