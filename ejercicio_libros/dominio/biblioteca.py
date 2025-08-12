import numpy as np

class Biblioteca():

    def __init__(self, cant):
        self.__estanteria = np.full(cant, None, dtype=object)

    def get_estanteria(self):
        return self.__estanteria

    def agregar_libro(self, libro):
        aux = False
        for i in range(self.__estanteria.size):
            if self.__estanteria[i] is None:
                self.__estanteria[i] = libro
                aux = True
        return aux


            
        
