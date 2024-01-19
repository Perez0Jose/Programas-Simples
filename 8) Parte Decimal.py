#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.


import math 

numero = float(input("Ingrese un numero con decimal"))
print("El número es: ", numero)
parte_decimal, parte_entera = math.modf(numero)
print("Su parte entera es {} y su parte decimal es {}".format(
    parte_entera, parte_decimal))



