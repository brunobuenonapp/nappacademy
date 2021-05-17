from massa_dados import list_spend_money


def spend_by_login(login, limit=1000):
    
    for item in list_spend_money:
        if login in item[1]:
            try:
                if type(item[3]) == str and item[3] != '':
                        num = float(item[3])
                        if num <= limit:
                            print(item)
                if type(item[3]) == float:
                    if item[3] <= limit:
                        print(item)                  
            except TypeError:
                raise TypeError('Erro') 


def sum_by_login(login, limit=1000):
    
    valor = 0

    for item in list_spend_money:
        if login in item[1]:
            try:
                if type(item[3]) == str and item[3] != '':
                    num = float(item[3])
                    if num <= limit:
                        valor += num
                if type(item[3]) == float:
                    if item[3] <= limit:
                        valor += item[3]                  
            except TypeError:
                raise TypeError('Erro')           

    return round(valor,2) 


if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login, 1200)
    print('A soma total até 1000: ')
    print(sum_by_login(login))
    print('A soma total até 1200: ')
    print(sum_by_login(login, 1200))
