from datetime import datetime

class Conta:
    def __init__(self, cliente, numero, saldo, limite):
        self.numero = str(numero)
        self.saldo = saldo
        self.cliente = cliente
        self.limite = limite
        self.extrato = []
        self.historico_transferencia = []

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

    def transferir(self, conta_destino, valor):
        saldo_disponivel = self.saldo + self.limite

        if valor > 0 and saldo_disponivel >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')

            self.registrar_historico('Enviada', conta_destino.cliente, valor, data_atual)
            conta_destino.registrar_historico('Recebida', self.cliente, valor, data_atual)
            print(f'Transferência de R${valor:.2f} realizada com sucesso para {conta_destino.cliente}.')
        else:
            print("Transferência não realizada. Saldo insuficiente ou valor inválido.")

    def registrar_historico(self, tipo, conta_envolvida, valor, data):
        registro = {
            "tipo": tipo,
            "conta_envolvida": conta_envolvida,
            "valor": valor,
            "data": data
        }
        self.historico_transferencia.append(registro)

    def mostrar_historico(self):
        if not self.historico_transferencia:
            print("Nenhuma transferência foi realizada")
        else:
            print(f"\nHistórico de transferências de {self.cliente}:")
            for registro in self.historico_transferencia:
                tipo = registro['tipo']
                conta = registro['conta_envolvida']
                valor = registro['valor']
                data = registro['data']
                print(f"{tipo}: R${valor:.2f} - {conta} - Data: {data}")
