#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo. El promedio del ramo se calcula con la siguiente formula.
# NC=(C1+C2+C3)3
#NF=NC⋅0.7+NL⋅0.3
#Donde NC
 #es el promedio de certámenes, NL
 #el promedio de laboratorio y NF
 #la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60

c1 = float(input("Ingrese la nota del primer examen: "))
c2 = float(input("Ingrese la nota del segundo examen: "))
nl = float(input("Ingrese la nota del laboratorio: "))


nc = (59.5 - 0.3 * nl) / 0.7
c3 = 3 * nc - (c1 + c2) + 1

print("Necesita nota", int(round(c3)), "en el certamen 3")

