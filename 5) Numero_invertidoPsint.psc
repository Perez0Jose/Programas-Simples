Proceso Numero_Invertido
	Definir num1,num_invertido,d Como Entero;

	Escribir "Por favor ingresar un numero entero de 3 digitos: ";
	Leer num1;
	num_invertido<-0;
	
	Mientras num1<>0 Hacer
		d = num1 % 10;
		num1=trunc(num1/10);
		num_invertido<-num_invertido*10+d
	FinMientras
	
	Escribir "Su numero invertido es asi ",num_invertido;
			
		
FinProceso
