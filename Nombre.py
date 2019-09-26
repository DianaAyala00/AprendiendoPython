nombre=input("Nombre:")
apellidos=input("Apellidos:")
#Se usaran varables de tpo string para almacenar nombre y apellidos, en la linea 5
#se ustan "" para separar el nombre de los apellidos
nombreCompleto=nombre+" "+apellidos
#A la variable nombreCompleto se le asigna un .upper() para volver mayusculas a los datos que almacene
nombreCompleto=nombreCompleto.upper()
print(nombreCompleto)