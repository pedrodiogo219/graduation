#include<bits/stdc++.h>
using namespace std;

int initial_points[100100];

class Union_Find{
  public:
  int * parent;
  int * points;
  int n;

  Union_Find(int n){
    this->n = n;
    this->parent = (int *) malloc( (n+5) * sizeof(int));
    this->points = (int *) malloc( (n+5) * sizeof(int));
    for(int i = 0; i < n ; i++){
      this->parent[i] = i;
      this->points[i] = initial_points[i];
    }
  }

  void printa(){
    for(int i = 0; i < this->n; i++){
      printf("%d ", this->parent[i]);
    }
    printf("\n");

    for(int i = 0; i < this->n; i++){
      printf("%d ", this->points[i]);
    }
    printf("\n\n");
  }

  int find(int a){

    int root = a;
    while(root!=this->parent[root]){
      root = this->parent[root];
    }

    int prox;
    while(a != root){
      prox = this->parent[a];
      this->parent[a] = root;
      a = prox;
    }

    return root;
  }

  int unify(int a, int b){
      int root_a = this->find(a);
      int root_b = this->find(b);

      if(root_a == root_b) return -1;

      if (root_a > root_b)
        swap(root_a, root_b);

      this->parent[root_b]  = this->parent[root_a];
      this->points[root_a] += this->points[root_b];

      return root_a;
  }

};

int main(){
  int option, a, b;

  while(true){
    int n, m;

    scanf("%d %d", &n, &m);
    if(n==0 && m == 0) return 0;


    for(int i = 0; i < n;i++){
      scanf("%d", &initial_points[i]);
    }

    Union_Find my_union = Union_Find(n);

    int wins = 0;
    while(m--){
      scanf("%d %d %d", &option, &a, &b);
      if(option==1){
        my_union.unify(a-1, b-1);
      }
      if(option==2){
        int guild_a = my_union.find(a-1);
        int guild_b = my_union.find(b-1);

        int my_guild = my_union.find(0);

        if(my_guild == guild_a && my_union.points[guild_a] > my_union.points[guild_b])
          wins+=1;

        if(my_guild == guild_b && my_union.points[guild_b] > my_union.points[guild_a])
          wins+=1;
      }
    }

    printf("%d\n", wins);

  }







}
