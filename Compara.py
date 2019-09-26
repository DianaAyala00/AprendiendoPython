numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida="Numeros proporcionados: {} y {}. {}."
if (numero1==numero2):
    #En las lineas anteriores se pide al usuario que de dos numeros
    #Despues se usa una condicion
    #Al final se imprimira el resultado  si la condicion se cumple y los dos numeros son iguales
    print(salida.format(numero1, numero2, "Los numeros son iguales"))
else:
    #Se agrega una condicion anidada, if dentro de otro if
    #Aqui señala cuando los numeros no son iguales
    if numero1>numero2:
        #Imprime por salida que el primer numero es mayor al segundo
        print(salida.format(numero1, numero2, "El mayor es el primero"))
    else:
        #Imprime por salida que el segundo numero es mayor
        print(salida.format(numero1, numero2, "El mayor es el segundo"))