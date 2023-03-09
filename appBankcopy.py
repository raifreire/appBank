dataList = []
data = {}
depositList = []
print('*'*10,'Bem vindo ao seu Banco','*'*10)
while True:
    print('1 - para Criar conta\n2 - para deposito\n3 - para saque\n4 - para ver saldo\n0 - para sair')
    condition = int(input("Qual a opção desejada: "))

    if condition == 1:
        while True:
            name = str(input('Digite o nome do Titular: '))
            cpf = str(input('Digite o cpf do Titular: '))
            data["name"] = name
            data["cpf"] = cpf
            dataList.append(data.copy())
            data.clear
            condition = str(input("Deseja cadastrar nova conta s/n? "))
            if condition == 'n':
                break
    elif condition == 2:
        while True:
            validate = str(input("Qual o cpf do titular da conta: "))
            for i, v in enumerate (dataList):
                if validate in v['cpf']:
                    amount = 0
                    while True:
                        deposit = float(input('Qual o valor do deposito? '))
                        amount = amount + deposit
                        dataList[i]['saldo'] = amount
                        condition = str(input('Novo deposito s/n'))
                        if condition == 'n':
                            break
            break
    elif condition == 3:
            validate = str(input("Qual o cpf do titular da conta: "))
            for i, v in enumerate (dataList):
                if validate in v['cpf']:
                    amount = 0
                    while True:
                        withdraw = float(input('Qual o valor do saque? '))
                        dataList[i]['saldo'] -= withdraw
                        condition = str(input('Novo saque s/n'))
                        if condition == 'n':
                            break
                break
    elif condition == 4:
            validate = str(input("Qual o cpf do titular da conta: "))
            for i, v in enumerate (dataList):
                if validate in v['cpf']:
                    print(dataList[i]['saldo'])
                break
    elif condition == 0:
        break
print(dataList)
