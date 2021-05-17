import datetime
tempo = datetime.date.today()
dia = None
mes = None
ano = None

while True:
    try:
        if not dia:
            dia = int(input('Dia de Nascimento: '))
            if dia >= 1 and dia <= 31:
                pass
            else:
                raise()
        if not mes:
            mes = int(input('Mês de Nascimento: '))
            if mes >= 1 and mes <= 12:
                pass
            else:
                raise()
        if not ano:
            ano = int(input('Ano de nascimento: '))
        break
    except:
        print('Digite corretamente a data, com apenas números.')

tempo2 = datetime.date(day=dia, month=mes, year=ano)
diferenca = tempo - tempo2
print('Você ja tem', diferenca.days, 'dias de vida!')