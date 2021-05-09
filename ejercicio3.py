#Escribe un programa en Python que reciba 5 números enteros del usuario y los guarde en una lista. Luego recorrer la lista y mostrar los números por pantalla.

numero1 = int(input("Ingrese su 1er número: "))

numero2 = int(input("Ingrese su 2do número: "))

numero3 = int(input("Ingrese su 3ero número: "))

numero4 = int(input("Ingrese su 4to número: "))

numero5 = int(input("Ingrese su 5to número: "))

lista_numeros = [numero1, numero2, numero3, numero4, numero5]

for numero in lista_numeros:
    print(numero)

