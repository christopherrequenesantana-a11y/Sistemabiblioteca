

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

def buscar_libro():
    nombre = input("Ingrese el libro a buscar: ")

    if nombre in libros:
        print("Libro encontrado.")
    else:
        print("Libro no encontrado.")

def eliminar_libro():
    nombre = input("Ingrese el libro a eliminar: ")

    if nombre in libros:
        libros.remove(nombre)
        print("Libro eliminado.")
    else:
        print("Libro no existe.")

# Menú principal
while True:

    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Registrar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Eliminar libro")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_libro()

    elif opcion == "2":
        mostrar_libros()

    elif opcion == "3":
        buscar_libro()

    elif opcion == "4":
        eliminar_libro()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
