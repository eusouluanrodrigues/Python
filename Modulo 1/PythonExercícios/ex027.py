nome = str(input("Digite seu nome completo: ")).strip()
print(('Muito prazer em te conhecer!'))
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print(('Seu ultimo nome é {}'.format(nome.split()[-1]))) # ou .format(nome[len](nome-1))
