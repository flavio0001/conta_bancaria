import random
from datetime import datetime

lista_contas = []

def gerar_numero_conta():
    while True:
        numero_gerado = random.randint(10000, 99999)
        if all(conta.numero != str(numero_gerado) for conta in lista_contas):
            return numero_gerado

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
