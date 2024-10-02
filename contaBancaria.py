
class Conta:
    def __init__(self, cliente, numero, saldo, limite):
        self.numero = str(numero)
        self.saldo = saldo
        self.cliente = cliente
        self.limite = limite
        self.extrato = []

    def saque(self, valor):
        saldo_total = self.saldo + self.limite
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append("- Saque: " + str(valor))
            return valor
        elif valor <= saldo_total:
            confirmacao = input(f"O valor de {valor} excede seu saldo disponível. Deseja usar o limite de cheque especial? (s/n): ")
            if confirmacao.lower() == 's':
                self.saldo -= valor
                self.extrato.append("- Saque: " + str(valor) + " (usando cheque especial)")
                return valor
            else:
                print("Operação cancelada.")
                return None
        else:
            print('Saldo insuficiente, mesmo com o uso do cheque especial.')

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append("+ Deposito: " + str(valor))

    def mostrar_extrato(self):
        print('------Extrato------')
        print('Conta: ', self.numero)
        for j in self.extrato:
            print(j)
        print('Saldo: ', self.saldo)
        print('Limite: ', self.limite)

    def __str__(self):
        return f"Conta {self.numero} - Cliente: {self.cliente} - Saldo: R${self.saldo:.2f}"