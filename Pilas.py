""" Crear pila """
historial = []

""" Agregar elementos a la pila """
historial.append("google.com")
historial.append("youtube.com")
historial.append("gitgub.com")


print("Historial: ", historial)

""" Ver elemento superior de la pila """
pagina_actual = historial[2]
print("Pagina actual: ", pagina_actual)

""" Eliminar elemento superior de la pila """
pagina_salida = historial.pop()
print("Pagina salida: ", pagina_salida)

print("Historial actualizado: ", historial)