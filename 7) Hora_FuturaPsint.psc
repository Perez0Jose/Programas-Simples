Algoritmo Hora_Futura
	Definir H_a,H_f Como Entero;
	Escribir "Ingrese la hora actual (en formato 24 horas): ";
	Leer H_a
	Escribir "Ingrese el numero de horas a avanzar: ";
	Leer H_f
	N_h<-(H_a+H_f) MOD 24
	Escribir "La hora despues de ",H_f," horas sera: ",N_h;
	
FinAlgoritmo
