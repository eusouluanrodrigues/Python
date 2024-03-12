import random
aleatorio = random.randint(0, 5)
print('Pensando....')
usuario = int(input('Em qual numero eu pensei? '))
if usuario == aleatorio:
    print('PARABENS VOCÊ VENCEU!')
else:
    print(('O computador VENCEU!'))


""" import random

# Gera um número aleatório entre 0 e 5
aleatorio = random.randint(0, 5)

print('Pensando....')

# Inicia um loop infinito
while True:
    # Pede ao usuário para adivinhar o número
    usuario = int(input('Em qual numero eu pensei? '))

    # Verifica se o palpite do usuário está correto
    if usuario == aleatorio:
        print('PARABÉNS VOCÊ ACERTOU!')
        break  # Sai do loop
    else:
        print('Que pena você errou, tente novamente!') """

# Nessa versão o codigo se repete ate o usuario acertar o numero escolhido pelo computador
