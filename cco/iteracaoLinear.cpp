#include<bits/stdc++.h>
using namespace std;


double f(double x, double y){
	return 0.2*x*x + 0.2*x*y + 0.6;
}

double g(double x, double y){
	return 0.4*x + 0.1*x*y*y + 0.5;
}

int main(){
	
	double x0 = 0.9;
	double y0 = 1.1;
	
	double erroX = 1e-5;
	double erroY = 1e-5;
	
	double x, y;
	int cont = 0;
	while(true){
		x = f(x0, y0);
		y = g(x0, y0);
		
		
		if(abs( x - x0 ) < erroX && fabs( y - y0 ) < erroY){
			break;
		}
		
		if(cont++ > 5000000) break;
		
		x0 = x;
		y0 = y;
	}
	
	printf("x=%.7lf y=%.7lf\n", x, y);
	
	
}
