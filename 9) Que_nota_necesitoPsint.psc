Algoritmo Que_nota_necesito
	Definir c1,c2,nl,nc,c3 Como Real;
	Escribir "Ingrese la nota del primer examen: ";
	Leer c1
	Escribir "Ingrese la nota del segundo examen: ";
	Leer c2
	Escribir "Ingrese la nota del laboratorio: ";
	Leer nl
	nc<- (59.5 - 0.3 * nl) / 0.7;
	c3<- 3* nc -(c1+c2) + 1;
	Escribir "Necesita nota ",redon(c3)," en el examen 3";
FinAlgoritmo
