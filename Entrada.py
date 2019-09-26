entrada=input()
print(type(entrada))
#Se ingresa una variable de tipo booleana que contiene el resultado
#si el dato capturado es un digito
#si el dato capturado es un numero entero, imprime el mensaje de la linea 8
esEntero=(entrada.isdigit() and entrada.find('.')==-1)
if (esEntero):
    print('El dato es entero. Excelente')
else:
    #De lo contrario, se imprime que hay que volver a ingresar el dato
    print('El dato no es entero. Inserta un dato nuevamente.')