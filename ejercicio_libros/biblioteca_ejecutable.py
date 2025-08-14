from dominio import libro

if __name__== "__main__":
    
    while True:
        cant = int(input("Ingrese la cantidad de libros de la biblioteca (>0) "))
        if cant > 0:
            break
    
    # Crear un arreglo que represente fisicamente el estante
    estanteria = []
    print(estanteria)

    for i in range(cant):
        isbn = input("Ingrese el ISBN del libro: ")
        autor = input("Ingrese el nombre del autor del libro: ")
        titulo = input("Ingrese el Titulo del libro: ")
        paginas = int(input("Ingrese el numero de paginas: "))
    
        libro_nuevo = libro.Libro(isbn, autor, titulo, paginas)
        estanteria.append(libro_nuevo)

    for i in range(len(estanteria)):
        print("Libro ", i+1, ": ", estanteria[i].__str__())