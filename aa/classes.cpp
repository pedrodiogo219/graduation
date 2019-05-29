#include<bits/stdc++.h>
using namespace std;

template<class T>
void ordena(vector<T> v, int n){
  for(int i=0;i<n;i++)
    cout << v[i] << ' ';

  cout << endl;
}

template<class T>
vector<T> cria_vector(){
  vector<T> v;
  return v;
}

int main(){

  vector<string> a;
  a.push_back("ahaha1");
  a.push_back("ahaha1");


  ordena(a, 1);

}
