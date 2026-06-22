# Sistema de Gestión de Biblioteca

libros = []

def registrar_libro():
    nombre = input("Ingrese el nombre del libro: ")
    libros.append(nombre)
    print("Libro registrado correctamente.")

def mostrar_libros():
    if len(libros) == 0:
        print("No existen libros registrados.")
    else:
        print("\nLista de libros:")
        for libro in libros:
            print("-", libro)

while True:
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Registrar libro")
    print("2. Mostrar libros")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_libro()
    elif opcion == "2":
        mostrar_libros()
    elif opcion == "3":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.")
