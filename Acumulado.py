#La variables se determinan con un int y un string
acumulado=int(0)
numero=str("")

#Se utiliza while para crar una condicion
#que sera un bucle hasta que el valor sea falso
#y aparezvca la intruccion break
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        #Si el numero da vacio significa que el programa termina
        print("Vacio. Salida del programa")
        break
    else:
        #Por el contrario si se recibe un numero
        #se realizara la suma incluyente
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))