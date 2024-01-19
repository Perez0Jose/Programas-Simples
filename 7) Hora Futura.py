#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

hora_actual = int(input("Ingrese la hora actual (en formato de 24 horas): "))
hora_futura = int(input("Ingrese el número de horas a avanzar: "))

nueva_hora = (hora_actual + hora_futura) % 24

print(f"La hora después de {hora_futura} horas será: {nueva_hora}")
