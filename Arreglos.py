#Declarando un arreglo
numeros = [10,20,30,40,50]

print (numeros[2])

#reasignar el valor del arreglo 3 
numeros[3]=15
print(numeros)

#Agreamos un valor nuevo al final del arreglo 
numeros.append(60)
print(numeros)

#Eliminar un valor de un arreglo

numeros.pop(2) #se coloca la posicion del valor en el arreglo
print(numeros)

#Eliminar un valor de un arreglo por valor
numeros.remove(15) #aqui va el valor que quieres eliminar 
print(numeros)


frutas =["mango", "manzana", "uva", "pera", "melon", "platano", "mandarina"]
frutas.remove("uva")
print(frutas)

frutas.pop(0)
print(frutas)

frutas.append("guayaba")
print(frutas)

frutas[1] = "papaya"
print(frutas)

#ingresar un valor a un arreglo
arreglo = []
n = int(input("Ingresa el tamaño del arreglo: "))

print(arreglo)