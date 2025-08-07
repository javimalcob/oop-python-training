
class CuentaBanco():

    def __init__(self, codigo : int, saldo: int, titular: str):
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
    def set_saldo(self, new_saldo):
        self.__saldo = new_saldo
    
    
    def get_titular(self):
        return self.__titular
    def set_titular(self, new_titular):
        self.__titular = new_titular