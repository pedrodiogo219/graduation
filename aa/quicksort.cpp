#include<bits/stdc++.h>
using namespace std;



int a[1000];

int cmp = 0;
bool comp (){
	cmp++;
	return true;
}

int trc = 0;
bool trocas(){
	trc++;
	return true;
}

void qs(int lo, int hi){
	if (lo >= hi) return;

	//cout << "lo: " << lo << " hi: " << hi << endl;

	int i = lo-1, j = hi;
	int v = a[hi], t;
	
	int it = 0;
	while(true){
		//cout << "it: " << ++it << endl;
		while(comp() && a[++i] < v){};
		while(comp() && a[--j] > v) if (j <= lo) break;

		if(i >= j) break;
		t = a[i]; a[i]=a[j]; a[j] = t; trocas();
	}

	t = a[i]; a[i] = v; a[hi] = t; trocas();

	qs(lo, i-1);
	qs(i+1, hi);
}

int main(){
	 std::srand ( unsigned ( std::time(0) ) );
	int x = 8;
	for(int i=0; i<x; i++) a[i] = i;
	random_shuffle(a, a+x);
	for(int i=0;i<x;i++) cout << " " << a[i];
	qs(0, x-1);

	/*
	for(int i=0;i<x;i++){
		if(i) cout << " " << a[i];
		else cout << a[i];
	}cout << endl;*/

	cout << "trocas: " << trc << endl;
	cout << "comparacoes: " << cmp << endl;
}
