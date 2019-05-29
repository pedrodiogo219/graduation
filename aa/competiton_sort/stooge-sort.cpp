#include<bits/stdc++.h>
using namespace std;
#define tipoInteiro 1
#define tipoFloat 2
#define tipoString 3

vector<string> entrada;

int define_tipo(){
	int max_linhas = entrada.size() < 5 ? entrada.size() : 5;

	bool eh_inteiro = true,
	 		 eh_float   = true;

 	for(int line=0; line < max_linhas; line++){
		for(int i=0; i < entrada[line].size(); i++){
			char c = entrada[line][i];

			if(c < '0' || c > '9')
				eh_inteiro = false;

			if( !( (c >= '0' && c<='9') || (c=='.') ) )
				eh_float = false;

			if(!eh_inteiro && !eh_float) break;
		}
	}

	if(eh_inteiro) return tipoInteiro;
	if(eh_float)   return tipoFloat;
	return tipoString;
}

template<class T>
T convert_to_type( string s ){
  istringstream stream(s);
  T res;
  stream >> res;
  return res;
}

template<class T>
void printa_vetor( vector<T> &v ){
	for(const auto item : v){
		cout << item << '\n';
	}
}


template<class T>
void stooge_sort(vector<T> &v, int lo, int hi){
  if( hi <= lo ) return;
  if(v[lo] > v[hi-1]) swap(v[lo], v[hi-1]);

  if(hi - lo > 2){
    int terco = (int) ((hi-lo) / 3);
    stooge_sort(v, lo, hi-terco);
    stooge_sort(v, lo+terco, hi);
    stooge_sort(v, lo, hi-terco);
		//merge(v, a, b, x, y);
  }
}

template<class T>
void ordena(vector<T> &v){
	stooge_sort<T>(v, 0, v.size());
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	string s;
	while(getline(cin, s)){
		entrada.push_back(s);
	}

	int tipoEntrada = define_tipo();
	if(tipoEntrada == tipoInteiro){
		vector<int> v;
		for(const auto item: entrada) v.push_back( convert_to_type<int>(item) );

		ordena<int>(v);
		printa_vetor(v);
	}

	else if(tipoEntrada == tipoFloat){
		vector<double> v;
		for(const auto item: entrada) v.push_back( convert_to_type<double>(item) );

		ordena<double>(v);
		printa_vetor(v);
	}

	else{
		vector<string> v = entrada;

		ordena<string>(v);
		printa_vetor(v);
	}

}
