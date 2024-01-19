#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#del triangulo, dado por el teorema de Pitágoras: c2=a2+b2


cateto_A = float(input("Ingrese el numero del primer cateto"))
cateto_B = float(input("Ingrese el numero del segundo cateto"))

H = cateto_A ** 2 + cateto_B ** 2

print(f"La hipotenusa de su triangulo es: {H}")

