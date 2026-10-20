from collections import deque

pila = []


def insertar_elemento(pila, elemento):
    pila.append(elemento)
    print(f"Elemento '{elemento}' insertado en la pila.")
    print(pila)


def mostrar_primer_elemento(pila):
    if not pila:
        print("La pila está vacía.")
        return
    primero = pila.pop()
    print(f"Primer elemento de la pila: {primero}")
    print(pila)


def listar_pila(pila):
    print("Elementos de la pila:")
    if not pila:
        print("La pila está vacía.")
        return
    for elemento in pila:
        print(elemento)


def menu():
    print("Seleccione una opción:")
    print("1. Insertar elemento en la pila")
    print("2. Mostrar primer elemento de la pila")
    print("3. Listar elementos de la pila")
    print("4. Salir")


def main():
    while True:
        menu()
        opcion = input("Ingresa el numero de la accion que deseas realizar: ")
        if opcion == "1":
            elemento = input("Ingresa el elemento que deseas insertar: ")
            insertar_elemento(pila, elemento)
        elif opcion == "2":
            mostrar_primer_elemento(pila)
        elif opcion == "3":
            listar_pila(pila)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    main()