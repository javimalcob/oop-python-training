from dominio import libro, biblioteca


if __name__== "__main__":
   

    #Crear un objeto biblioteca
    while True:
        cant = int(input("Ingrese la cantidad de libros de la biblioteca (>0) "))
        if cant > 0:
            break

    mi_biblioteca = biblioteca.Biblioteca(cant)

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

    if(mi_biblioteca.agregar_libro(libro1)):
        print("Libro agregado")
    else:
        print("No se puedo agregar el libro")

    mi_biblioteca.agregar_libro(libro2)
    
    #Mostrar estado de la biblioteca
    listado = mi_biblioteca.mostrar_listado()
    print(listado)
    #Resultados
    #print("Libro 1: ", libro1)
    #print("Libro 2:", libro2.__str__())

