lista_frases = ['Eu gosto de batatas', 'Eu estava andando de moto']
lista_frases += ['Ele estava comendo no restaurante']
lista_frases += ['O cachorro está passeando pelo parque']

nova_lista = []
for ctd in lista_frases:
    nova_lista.append(ctd.split(' '))
for ctd in nova_lista:
    for item in ctd:
        if 'ando' in item:
            print(item)
        if 'endo' in item:
            print(item)
        if 'indo' in item:
            print(item)
