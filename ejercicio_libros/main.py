from dominio import libro

if __name__== "__main__":
   

    libro1 = libro.Libro() 
    
    libro1.set_isbn("109523")
    libro1.set_paginas(1130)
    libro1.set_titulo("Noctem Girl")
    libro1.set_autor("Florencia")

    isbn2 = input("Ingrese el ISBN del libro: ")
    autor2 = input("Ingrese el nombre del autor del libro: ")
    titulo2 = input("Ingrese el Titulo del libro: ")
    paginas2 = int(input("Ingrese el numero de paginas: "))
    
    libro2 = libro.Libro(isbn2, autor2, titulo2, paginas2)

    #Resultados
    print("Libro 1: ", libro1)
    print("Libro 2:", libro2.__str__())

    if libro1.get_paginas() > libro2.get_paginas():
        print("Libro 1 con mas paginas")
    elif libro2.get_paginas() > libro1.get_paginas():
        print("Libro 2 con mas paginas")
    else:
        print("Ambos libros tienen la misma cantidad de paginas")