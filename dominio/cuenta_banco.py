
class CuentaBanco():

    def __init__(self, codigo=0, saldo=0.0, titular=''):
        # Atributos
        self.__codigo = codigo
        self.__saldo = saldo
        self.__titular = titular

    # Metodos/ Comportamientos: de acceso o accesores
    def get_codigo(self):
        return self.__codigo
    def set_codigo(self, new_cod):
        self.__codigo = new_cod


    def get_saldo(self):
        return self.__saldo

    
    def get_titular(self):
        return self.__titular
    def set_titular(self, new_titular):
        self.__titular = new_titular

    # Comportamiento propios: depositar() y extraer()

    def depositar(self, monto):
        if monto > 0:
            self.__saldo = self.__saldo + monto
            print("Se realizó exitosamente el depósito")

    def extraccion(self, monto):
        if monto > 0 and self.__saldo >= monto:
            self.__saldo = self.__saldo - monto
            print("Se realizó exitosamente la extracción")
        