#Se utiliza la funcion for donde se crea una tabla que contenga numeros del 1 a 10
for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #Se coloca un print sin texto
    print()
    #Se hace una iteracion con la funcion for
    for j in range(1,11):
        #i almacenara el numero de la tabla
        #y el dato j tendra el elemento de la tabla
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #Al finalizar con las iteraciones de las lineas anteriores
        #se ejecuta mostrando que hay un salto de linea
        #El resultado final muestra las tablas de multiplicar
        print()