import random
from contaBancaria import Conta
from datetime import datetime

lista_contas = []


def calcular_idade(data_nascimento):
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade


def solicitar_saldo_inicial():
    while True:
        try:
            saldo_inicial = float(input("Qual será o saldo que deseja depositar inicialmente: R$"))
            if saldo_inicial >= 1:
                return saldo_inicial
            else:
                print("O saldo não pode ser negativo ou igual a 0.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")


def solicitar_limite():
    while True:
        try:
            limite = float(input("Digite o limite de saque: R$"))
            if limite >= 0:
                return limite
            else:
                print("O limite não pode ser negativo. Por favor, insira um valor válido.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")


def listar_contas():
    if not lista_contas:
        print("Não há contas disponíveis.")
    else:
        print("Contas cadastradas:")
        for conta in lista_contas:
            print(conta)


def remover_conta():
    if not lista_contas:
        print("Não há contas para remover.")
    else:
        nome_conta_para_remover = input("Digite o nome do cliente cuja conta deseja remover: ")
        for conta in lista_contas:
            if conta.cliente == nome_conta_para_remover:
                lista_contas.remove(conta)
                print(f"Conta de {nome_conta_para_remover} removida com sucesso.")
                return
        print(f"Conta com o nome {nome_conta_para_remover} não encontrada.")


def verificar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) == 11 and cpf.isdigit():
        return True
    else:
        return False


def verificar_data(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        return data
    except ValueError:
        return None


def gerar_numero_conta():
    while True:
        numero_gerado = random.randint(10000, 99999)
        if all(conta.numero != str(numero_gerado) for conta in lista_contas):
            return numero_gerado


def cadastrar_conta():
    nome_cliente = str(input("Informe o nome e sobrenome do novo cliente: "))
    cpf = input("Digite os 11 números do seu CPF:")

    if not verificar_cpf(cpf):
        print("CPF inválido! Verifique novamente.")
        return

    data_nascimento = verificar_data(input("Digite data de nascimento no formato: (DD/MM/AAAA): "))
    if data_nascimento is None:
        print("Data de nascimento inválida!")
        return

    idade_cliente = calcular_idade(data_nascimento)
    if idade_cliente < 18:
        print("Não é possível abrir conta para menores de 18 anos.")
        return

    saldo_inicial = solicitar_saldo_inicial()
    limite = solicitar_limite()
    numero_conta = gerar_numero_conta()

    nova_conta = Conta(cliente=nome_cliente, numero=numero_conta, saldo=0, limite=limite)
    nova_conta.deposito(saldo_inicial)
    lista_contas.append(nova_conta)

    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    print(f"Saldo inicial: R${saldo_inicial:.2f} | Limite: R${limite:.2f}")


def extrato():
    nome_conta = input("Digite o nome do cliente que deseja obter o extrato da conta: ")
    conta_encontrada = False
    for conta in lista_contas:
        if conta.cliente == nome_conta:
            conta.mostrar_extrato()
            conta_encontrada = True
            break
    if not conta_encontrada:
        print("Conta não encontrada")


def efetuar_transferencia():
    nome_conta_origem = input("Digite o nome da conta de origem: ")
    conta_origem = None

    # Busca a conta de origem
    for conta in lista_contas:
        if conta.cliente == nome_conta_origem:
            conta_origem = conta
            break

    if conta_origem is None:
        print("Conta de origem não encontrada.")
        return

    print(f"Saldo atual da conta de origem ({conta_origem.cliente}): R${conta_origem.saldo:.2f}")

    nome_conta_destino = input("Digite o nome da conta destino que deseja efetuar a operação: ")
    conta_destino = None

    # Busca a conta de destino
    for conta in lista_contas:
        if conta.cliente == nome_conta_destino:
            conta_destino = conta
            break

    if conta_destino is None:
        print("Conta de destino não encontrada.")
        return

    # Solicita o valor a ser transferido
    try:
        valor = float(input("Qual o valor a ser transferido? R$"))
        if valor <= 0:
            print("O valor da transferência deve ser positivo.")
            return
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")
        return

    # Verifica se há saldo suficiente na conta de origem
    if conta_origem.saldo < valor:
        print(f"Saldo insuficiente para realizar a transferência. Saldo disponível: R${conta_origem.saldo:.2f}")
        return

    conta_origem.transferir(conta_destino, valor)


def submenu():
    opcoes = input("1 - Ver extrato da conta\n2 - Efetuar uma transferência\nDigite a opção: ")

    if opcoes == '1':
        extrato()
    elif opcoes == '2':
        efetuar_transferencia()


def menu_principal():
    while True:
        opc = input("1 - Cadastrar \n2 - Listar contas cadastradas \n3 - Remover cadastro\n4 - +Opções\nDigite uma opção: ")

        if opc == '1':
            cadastrar_conta()
        elif opc == '2':
            listar_contas()
        elif opc == '3':
            remover_conta()
        elif opc == '4':
            submenu()
