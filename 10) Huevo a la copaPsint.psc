Algoritmo Potencia
	Definir th,te,m,p,c,k,dividendo,divisor,resultado,resultado2,seg,min Como Real;
	Escribir "Temperatura original del huevo: ";
	Leer th;
	te<-100;
	m<-47;
	p<-1.038;
	c<-3.7;
	k<-0.0054;
	
	dividendo<-((m^(2/3)*3.7*(p^(1/3))));
	divisor<-(k*PI*PI*(4*PI/3)^(2/3));
	resultado<- dividendo/divisor;
	resultado2<-ln(0.76*((th-te)/(70-100)));
	seg<-resultado*resultado2;
	min<-redon(seg/60);
	
	Escribir "El tiempo maximo para prepararlo a la copa ",min," minutos"
	
FinAlgoritmo
