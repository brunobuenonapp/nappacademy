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
#30.436875
diferenca = tempo - tempo2
anos = int(str((diferenca.days/ 365.25)).split('.')[0])
anos_em_dias = int(str(anos*365.25).split('.')[0])
meses = int(str((diferenca.days-anos_em_dias)/30.436875).split('.')[0])
meses_em_dias = int(str(meses*30.436875).split('.')[0])
dias = diferenca.days-(anos_em_dias+meses_em_dias)-1

print('Você tem', anos, 'anos,', meses, 'meses, e', dias, 'dias.')