#se almacena un numero y se convierte a int
numero=int(input("Dame un numero entero:"))
#Se almacena como valor booleanos el resultado de los residuos. Si el residuo es cero significa
#que el numero es multiplo
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
#Se usa and para condicionar que se realice la operacion cuando el resultado sea verdadero
#y se usa el or cuando uno de los dos cumpla con las condiciones dadas
#Las primeras dos son juntas y la tercera es independiente su resultado
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto")
else:
    print("Incorrecto")