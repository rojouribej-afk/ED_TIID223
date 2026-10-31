
"""Clase que representa la estructura de un Nodo."""


class Nodo:
    def __init__(self, numero):
        """Valor que tendrá el nodo."""
        self.numero = numero
        """Apunta al siguiente nodo."""
        self.siguiente = None


class ListasEnlazadas:
    def __init__(self):
        self.cabeza = None

    def Insertar_Nodo_al_Inicio(self, numero):
        nuevo_nodo = Nodo(numero)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_final(self, numero):
        nuevo_nodo = Nodo(numero)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def Eliminar_Nodo_al_Inicio(self):
        if self.cabeza is not None:
            self.cabeza = self.cabeza.siguiente

    def Eliminar_Nodo_al_final(self):
        if self.cabeza is None:
            return

        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = None

    def Imprimir_listaEnlazada(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.numero, "→ ", end="")
            actual = actual.siguiente
        print("NONE")


Mi_lista = ListasEnlazadas()
Mi_lista.Insertar_Nodo_al_Inicio(5)
Mi_lista.Insertar_Nodo_al_Inicio(4)
Mi_lista.Insertar_Nodo_al_Inicio(3)
Mi_lista.Insertar_Nodo_al_final(6)
Mi_lista.Imprimir_listaEnlazada()
Mi_lista.Eliminar_Nodo_al_Inicio()
Mi_lista.Imprimir_listaEnlazada()
Mi_lista.Eliminar_Nodo_al_final()
Mi_lista.Imprimir_listaEnlazada()
