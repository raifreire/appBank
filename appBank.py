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
            for i in dataList:
                for k, v in i.items():
                    if validate == v:
                        amount = float(input('Qual o valor do deposito: '))
                        depositList.append(amount)
                        i['deposit'] = depositList[:]
                        depositList.clear()
                        print(i)
                        break
            condition = str(input("Deseja realizar novo deposito s/n? "))
            if condition == 'n':
                break
    
    elif condition == 0:
        break

print(dataList)
