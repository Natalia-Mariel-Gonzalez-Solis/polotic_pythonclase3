#Dada una lista (lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]), iterarla y mostrar números divisibles por cinco, si encuentra un número mayor que 150, detenga la iteración del bucle.

lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for numero in lista1:
    if numero > 150:
        print("Encontré un número mayor a 150 ¡Fin!")
        break
    elif numero % 5 == 0:
        print(numero)