from massa_dados import list_spend_money
             
def spend_by_login(login):

        for item in list_spend_money:
                if item[1] == login:
                        print(item)
                
        
def sum_by_login(login):
        valor = 0
        for item in list_spend_money:
                if item[1] == login:
                    try:
                        if type(item[3]) == float:
                            valor += item[3]
                        if type(item[3]) == str and item[3] != '':
                            valor += float(item[3])
                    except TypeError:
                        raise TypeError('Formato inválido!')            
        return round(valor,2)


if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login)
    print('A soma total é: ')
    print(sum_by_login(login))

