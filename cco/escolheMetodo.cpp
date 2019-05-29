#include<bits/stdc++.h>
using namespace std;


double f(double lambda){
	return 1564000.0 - ( (1000000.0*exp(lambda)) + (435000.0/lambda)*(exp(lambda) - 1) );
}

int main(){
	
	double a, b, meio;
	double erro;
	double Fmeio;

	a = 0.0000001;
	b = 2.0;
	erro = 0.0001;

	int cont= 0;
	while(true){
		meio = (a+b)/2.0;

		Fmeio = f(meio);

		printf("a: %.5lf\tmeio: %.5lf\tb: %.5lf\tFmeio: %.5lf\n", a, meio, b, Fmeio);
		
		if(fabs(Fmeio) < erro) break;

		if(cont++ > 100) break;

		if(f(a)*Fmeio < 0){
			b = meio;
		}else{
			a = meio;
		}
	}	
	
	printf("lambda: %.10lf\n", meio);
}
