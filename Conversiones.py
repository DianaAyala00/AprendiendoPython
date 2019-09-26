#Se declara la variable de tipo string, ya que seran numeros
numero="1234"
# de declarar variables se imprime una salida con type()
print(type(numero))
#La variable se convierte en su equivalencia en int
numero=int(numero)
print(type(numero))
#se imprime el resultado final, luego de convertir la variable con type
#el valor del numero se colocara dentro de las llaves
salida= "El numero utilizado es {}"
#se imprime una variable de tipo str la cual tendra la funcion
#da una salida de los valores utilizando la funcion format
print(salida.format(numero))