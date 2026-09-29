matriz = [
    [1,2,3],
    [4,5,6]
]

""" Muestra todo el arreglo, el for lo muestra ordenado, una fila abajo de otra """
print("Mostrar arreglo")
for fila in matriz:
    print(fila)
    
""" Muestra un determinado valor del arreglo """  
 
print("Mostrar 6")
print(matriz[1][2])


""" Se muestra la fila 0 """
print(matriz[0])

""" Reasignación de un valor del arreglo """
matriz[1][1] = 8
print(matriz)

""" Añadir una fila al arreglo """
matriz.append([7,8,9])
print(matriz)

""" Eliminar un valor  """
matriz[0].pop(2)
print(matriz)