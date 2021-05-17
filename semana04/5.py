import csv
import datetime

def carregar_arquivo():
    global lista
    lista = []
    with open('usernames.csv', newline='\n') as a:
        ler = csv.reader(a, delimiter=',', quotechar='|')
        for linha in ler:
            lista.append(linha)

def find_born_monday(parametro=0):
    dias_semanas = dict(zip(['segunda', 'segunda-feira', 'terça', 'terça-feira', 'quarta', 'quarta-feira',
              'quinta', 'quinta-feira', 'sexta', 'sexta-feira', 'sabado', 'domingo'],
                            ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '6']))
    for linha in lista:
        try:
            dia = int(linha[-2].split('-')[2])
            mes = int(linha[-2].split('-')[1])
            ano = int(linha[-2].split('-')[0])
            data = datetime.date(day=dia, month=mes, year=ano)
            if data.weekday() == dias_semanas.get(parametro, parametro):
                print(linha[0])
        except: continue

carregar_arquivo()
find_born_monday(0)