from contaBancaria import Conta
from funcoes import gerar_numero_conta, lista_contas, verificar_cpf, verificar_data
from datetime import datetime

print("------ Menu Principal ------")

def calcular_idade(data_nascimento):
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def menu_principal():
    while True:
        opc = int(input("1 - Cadastrar \n2 - Listar contas cadastradas \n3 - Remover cadastro\nDigite uma opção: "))

        if opc == 1:
            nome_cliente = str(input("Informe o nome e sobrenome do novo cliente: "))
            cpf = input("Digite os 11 números do seu CPF:")

            if verificar_cpf(cpf):
                print("CPF cadastrado na base de dados")
            else:
                print("CPF inválido! Verifique novamente")
                break

            data_nascimento = verificar_data(input("Digite data de nascimento no formato: (DD/MM/AAAA): "))

            if data_nascimento is None:
                print("Data de nascimento inválida!")
                break

            idade_cliente = calcular_idade(data_nascimento)

            if idade_cliente < 18:
                print("Não é possível abrir conta para menores de 18 anos.")
                break
            else:
                print("Vamos dar continuidade.")

            while True:
                saldo_inicial = float(input("Qual será o saldo que deseja depositar inicialmente: R$"))
                if saldo_inicial >= 1:
                    break
                else:
                    print("O saldo não pode ser negativo ou igual a 0")

            while True:
                limite = float(input("Digite o limite de saque: R$"))
                if limite >= 0:
                    break
                else:
                    print("O limite não pode ser negativo. Por favor tente novamente.")

            numero_conta = gerar_numero_conta()

            nova_conta = Conta(cliente=nome_cliente, numero=numero_conta, saldo=0, limite=limite)
            nova_conta.deposito(saldo_inicial)

            lista_contas.append(nova_conta)

            print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
            print(f"Saldo inicial: R${saldo_inicial:.2f} | Limite: R${limite:.2f}")


        elif opc == 2:
            if not lista_contas:
                print("Não há contas disponíveis.")
            else:
                print("Contas cadastradas:")
                for conta in lista_contas:
                    print(conta)

        elif opc == 3:
            if not lista_contas:
                print("Não a contas para remover")
            else:
                nome_conta_para_remover = input("Digite o nome da conta que deseja remover: ")
                conta_encontrada = False
                for contas in lista_contas:
                    if conta.cliente == nome_conta_para_remover:
                        lista_contas.remove(conta)
                        conta_encontrada = True
                        print(f"Conta de {nome_conta_para_remover} removida com sucesso")
menu_principal()
