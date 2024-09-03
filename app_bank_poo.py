class ContaBancaria:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso.')

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')

    def exibir_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')


class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, nome, cpf):
        nova_conta = ContaBancaria(nome, cpf)
        self.contas.append(nova_conta)
        print('Conta criada com sucesso.')

    def encontrar_conta_por_cpf(self, cpf):
        for conta in self.contas:
            if conta.cpf == cpf:
                return conta
        return None

    def menu(self):
        while True:
            print('*' * 10, 'Bem vindo ao seu Banco', '*' * 10)
            print('1 - para Criar conta\n2 - para deposito\n3 - para saque\n4 - para ver saldo\n0 - para sair')
            opcao = int(input("Qual a opção desejada: "))

            if opcao == 1:
                while True:
                    nome = str(input('Digite o nome do Titular: '))
                    cpf = str(input('Digite o cpf do Titular: '))
                    self.criar_conta(nome, cpf)
                    continuar = str(input("Deseja cadastrar nova conta s/n? "))
                    if continuar.lower() == 'n':
                        break
            elif opcao == 2:
                cpf = str(input("Qual o cpf do titular da conta: "))
                conta = self.encontrar_conta_por_cpf(cpf)
                if conta:
                    while True:
                        valor = float(input('Qual o valor do deposito? '))
                        conta.depositar(valor)
                        continuar = str(input('Novo deposito s/n? '))
                        if continuar.lower() == 'n':
                            break
                else:
                    print('Conta não encontrada.')
            elif opcao == 3:
                cpf = str(input("Qual o cpf do titular da conta: "))
                conta = self.encontrar_conta_por_cpf(cpf)
                if conta:
                    while True:
                        valor = float(input('Qual o valor do saque? '))
                        conta.sacar(valor)
                        continuar = str(input('Novo saque s/n? '))
                        if continuar.lower() == 'n':
                            break
                else:
                    print('Conta não encontrada.')
            elif opcao == 4:
                cpf = str(input("Qual o cpf do titular da conta: "))
                conta = self.encontrar_conta_por_cpf(cpf)
                if conta:
                    conta.exibir_saldo()
                else:
                    print('Conta não encontrada.')
            elif opcao == 0:
                break
            else:
                print('Opção inválida.')

# Criação do banco e execução do menu
banco = Banco()
banco.menu()
