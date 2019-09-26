numero=input("Dame un numero del 1 al 9:")
numero=int(numero)
#Inicia con un mensaje donde se pide un numero del 1 al 9
#despues con la funcion for se indica un bucle donde se pide que de un rango de valores.
for i in range(1,11):
    #i es el dato que va a variar conforme den los datos
    salida="{} x {} = {}"
    #se imprime el listado de los numeros multiplicados y el resultado final
    print(salida.format(numero,i,i*numero))