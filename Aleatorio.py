#Aqui se esta utilizando una forma de almacenar datos
#para usar la funcion se pone import
import random
#se declara una float como una variable y ya se le da un valor determinado
numero1=float(10.5)
#En la linea 8 estamos usando una definición de función para crear funciones creadas por el usuario
#lo que esta a la derecha es parte de la funcion def
def miFuncion():
    #Se convierte a float el numero aleatorio generado por
    #random.randrange()
    numero2=float(random.randrange(1,10))
    #Se utilizan llaves para gardar los datos y poder usar las variables
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))
#Al final se ejecuta la funcion con los datos que el usuario dio
miFuncion()