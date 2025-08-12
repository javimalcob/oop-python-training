class Libro():
    
    def __init__(self, isbn='Sin ISBN', autor='Desconocido', titulo='Desconocido', paginas=1):
        self.__isbn = isbn
        self.__autor = autor
        self.__titulo = titulo
        self.__paginas = self.__validar_paginas(paginas)

    def get_isbn(self):
        return self.__isbn
    def set_isbn(self,isbn):
        self.__isbn = isbn

    def get_autor(self):
        return self.__autor
    def set_autor(self, autor):
        self.__autor = autor
    
    def get_titulo(self):
        return self.__titulo
    def set_titulo(self, titulo):
        self.__titulo = titulo        

    def get_paginas(self):
        return self.__paginas
    def set_paginas(self, paginas):
        self.__paginas = self.__validar_paginas(paginas)

    def __str__(self):
        return f"El libro con ISBN {self.__isbn}, creado por el autor: {self.__autor} tiene: {self.__paginas} paginas."

    #Defino un metodo privado para validar paginas
    def __validar_paginas(self, paginas):
        return paginas if paginas > 0 else 1