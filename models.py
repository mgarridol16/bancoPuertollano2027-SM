import os

from logs import Log

log = Log()


class CuentaBancaria:

    def __init__(self, saldo=0.0):
        self.saldo = float(saldo)

    def getSaldo(self):
        return self.saldo

    def ingresar(self, cantidad):
        if cantidad <= 0:
            return False
        self.saldo += cantidad
        log.escribir("INFO", f"Ingreso de {cantidad}€ realizado en la cuenta bancaria.")
        return True

    def retirar(self, cantidad):
        if cantidad <= 0:
            return False
        self.saldo -= cantidad
        log.escribir("INFO", f"Retirada de {cantidad}€ realizado en la cuenta bancaria.")
        return True


class Deposito:

    def __init__(self, saldo=0.0):
        self.saldo = float(saldo)

    def ingresar(self, cantidad):
        if cantidad <= 0:
            return False
        self.saldo += cantidad
        log.escribir("INFO", f"Ingreso de {cantidad}€ realizado en la cuenta bancaria.")

        return True

    def retirar(self, cantidad):
        if cantidad <= 0:
            return False
        self.saldo -= cantidad
        log.escribir("INFO", f"Retirada de {cantidad}€ realizado en la cuenta bancaria.")

        return True

    def getSaldo(self):
        return self.saldo


class Cliente:

    def __init__(self, numero):
        self.numero = numero
        self.cuenta = CuentaBancaria()
        self.deposito = Deposito()

    def getNumero(self):
        return self.numero

    def getCuenta(self):
        return self.cuenta

    def getDeposito(self):
        return self.deposito

    def getSaldoTotal(self):
        return self.cuenta.getSaldo() + self.deposito.getSaldo()

    def guardar(self):
        if not os.path.exists("datosClientes"):
            os.mkdir("datosClientes")

        with open(f"datosClientes/{self.numero}.txt", "w") as f:
            f.write(
                f"{self.numero}\n"
                f"{self.cuenta.getSaldo()}\n"
                f"{self.deposito.getSaldo()}\n"
            )
