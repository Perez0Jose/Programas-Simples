#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso

Entero = int(input("Por favor ingresar un numero entero de 3 digitos"))
numero_invertido = str(Entero)[::-1]
print(f"su numero invertido es asi {numero_invertido}")