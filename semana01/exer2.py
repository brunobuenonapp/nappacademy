lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'elen']
vogais = ['A', 'E', 'I', 'O', 'U']

for nome in lista_nomes:
    teste = nome[0].upper()
    if teste in vogais:
        print(nome)
