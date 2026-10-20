from collections import deque

cola = deque()


def insertar_elemento(cola, elemento):
    cola.append(elemento)
    print(f"Elemento '{elemento}' insertado en la cola.")
    print(cola)


def mostrar_primer_elemento(cola):
    if not cola:
        print("La cola está vacía.")
        return
    primero = cola.popleft()
    print(f"Primer elemento de la cola: {primero}")
    print(cola)


def listar_cola(cola):
    print("Elementos de la cola:")
    if not cola:
        print("La cola está vacía.")
        return
    for elemento in cola:
        print(elemento)


def menu():
    print("Seleccione una opción:")
    print("1. Insertar elemento en la cola")
    print("2. Mostrar primer elemento de la cola")
    print("3. Listar elementos de la cola")
    print("4. Salir")


def main():
    while True:
        menu()
        opcion = input("Ingresa el numero de la accion que deseas realizar: ")
        if opcion == "1":
            elemento = input("Ingresa el elemento que deseas insertar: ")
            insertar_elemento(cola, elemento)
        elif opcion == "2":
            mostrar_primer_elemento(cola)
        elif opcion == "3":
            listar_cola(cola)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    main()