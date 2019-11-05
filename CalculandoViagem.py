#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distância da viagem em KM: '))
preco_passagem = (distancia*0.50)
adicional = (distancia*0.45)


if distancia <= 200:
    print(f'A passagem é de {preco_passagem}R$.')
else:
    print(f'Passando de 200KM de viagem você recebeu o desconto de 0,45R$ a viagem. Valor total de {adicional}R$.')