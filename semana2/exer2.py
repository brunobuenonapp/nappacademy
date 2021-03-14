from massa_dados import list_spend_money


def spend_by_gender(gender):
    
    for item in list_spend_money:
                if item[2] == gender:
                        print(item)


def sum_by_gender(gender):
    
    valor = 0
    
    for item in list_spend_money:
        if item[2] == gender:
            try:
                if type(item[3]) == float:
                    valor += item[3]
                if type(item[3]) == str and item[3] != '':
                    valor += float(item[3])
            except TypeError:
                raise TypeError('Formato inválido!')
            
    return round(valor,2)


if __name__ == "__main__":
    gender = 'M'
    spend_by_gender(gender)
    print('A soma total é: ')
    print(sum_by_gender(gender))

