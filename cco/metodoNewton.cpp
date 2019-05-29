#include<bits/stdc++.h>
using namespace std;


double F(double x, double y){
	return x - (( (x*x + y*y - 2)*(-2*y) - (x*x - y*y - 1)*(2*y)  )/(-8*x*y));
}


double G( double x, double y ){
	return y - ((  (x*x - y*y -1)*(2*x) - (x*x + y*y - 2)*(2*x)  )/(-8*x*y));
}

int main(){
	
	double x, x0, y, y0;
	double erro = 1e-5;
	
	
	x0 = 1.0;
	y0 = 1.0;
	int cont = 0;
	while(true){
		x = F(x0, y0);
		y = G(x0, y0);
		
		if( fabs(x-x0) < erro && fabs(y-y0) < erro ) break;
		
		if(cont++ > 5000000) break;
		
		x0 = x;
		y0 = y;
		
	}	
	
	printf("x=%.7lf   y=%.7lf\n", x, y);
		
}
