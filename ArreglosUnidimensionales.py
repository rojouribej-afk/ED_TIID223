""" numeros = [10,20,30,40,50]

print(numeros[2]) """

""" numeros = [10,20,30,40,50]
numeros[2]= 100
print(numeros) """

""" numeros = [10,20,30,40,50]
numeros.append([60,70])
print(numeros)
 """

""" numeros = [10,20,30,40,50]
numeros.append(60)
numeros.append(70)
print(numeros)
 """

""" 
numeros = [10,20,30,40,50]
numeros.append([60,70])
print(numeros[5]) """

""" numeros = [10,20,30,40,50]
numeros.insert(2, 25)
print(numeros)
 """

""" 
numeros = [10,20,30,40,50]
numeros = numeros + [50]
print(numeros) """


""" numeros = [10,20,30,40,50]
numeros = numeros +[50,60,70]
print(numeros) """

""" numeros = [10,20,30,40,50]
numeros[len(numeros):] = [40]
print(numeros)
 """

""" calificaciones = [70, 85, 90, 65]
calificaciones.append(95)
print (calificaciones)
 """
 
""" calificaciones = [70, 85, 90, 65]
calificaciones.insert(2, 80) 
print (calificaciones)
 """
 
"""colores = ["azul", "amarillo", "rosa"]
colores.append("verde")
colores.append("morado")
colores.append("rosa")
 print(colores) 

colores.append("negro")
print(colores[6])"""

numeros = [10,20,30,40]
numeros.insert(2,95)
numeros.append(50)
numeros.append(67)
print(numeros[6])

for pos, numeros in enumerate(numeros):
    print(f"El numero {numeros} esta en la posicion {pos}")