#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <vector>

using namespace std;

vector<int> v;

void stooge_sort(int lo, int hi){
  if( hi <= lo ) return;
  if(v[lo] > v[hi-1]) swap(v[lo], v[hi-1]);

  if(hi - lo > 2){
    int terco = (int) ((hi-lo) / 3);
    stooge_sort(lo, hi-terco);
    stooge_sort(lo+terco, hi);
    stooge_sort(lo, hi-terco);
  }
}

void show_vetor(){
  for(const auto it : v){
    printf("%d ", (it));
  }
  printf("\n");
}

int main(){
  int x;
  while(scanf("%d", &x)!=EOF){
    v.push_back(x);
  }

  stooge_sort(0, v.size());
  show_vetor();

}
