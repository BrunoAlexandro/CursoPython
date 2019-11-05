n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 5 and media < 7:
    print('Você está em recuperação.')
elif media >= 7:
    print('Você está aprovado.')
elif media <= 5:
    print('Você está reprovado.')
