
import java.util.ArrayList;
import java.io.*;

/*
*sort: sortear permutaÃ§Ã£o uniformemente aleatÃ³ria
/sort: inteiros ordenados de modo crescente
\sort: inteiros ordenados de modo decrescente
\/sort: cenÃ¡rio de pior caso para uma implementaÃ§Ã£o do quicksort com mediana de 3 [3,2,1,0,0,1,2,3]
/\sort: sobe e desce
3sort: crescente com apenas trÃªs nÃºmeros desordenados
+sort: crescente com 10 nÃºmeros do tipo ponto-flutuante aleatÃ³rios no fim
%sort: crescente e troca aleatoriamente 1% dos inteiros por valores aleatorios
csort: inteiros desordenados em blocos de atÃ© c elementos
=sort: todos iguais
~sort: inteiros com muitas repetiÃ§Ãµes
01sort: sÃ³ bits (0 ou 1)
01*sort: strings binÃ¡rios de comprimento aleatÃ³rio atÃ© 100
ACTGsort: sequÃªncias de DNA de comprimento aleatÃ³rio atÃ© 200
PTsort: frases compostas por conjuntos de palavras do portuguÃªs sorteadas aleatoriamente (atÃ© 10 palavras)
*/
public class Generator {

  // PTsort
  static String[] getPTsort(int n) throws Exception {
    String[] v = new String[n];

    BufferedReader br = new BufferedReader(new FileReader("Lista-de-Palavras.txt"));
    ArrayList<String> dicionario = new ArrayList<>(29858);

    while (br.ready()) dicionario.add(br.readLine());

    int W = dicionario.size();

    for (int i = 0; i < n; i++) {
      int l = 1+(int)(Math.random() *(10));
      v[i]= "";
      for (int j = 0; j < l ; j++) {
        int w = (int)(Math.random() *W);
        v[i] += dicionario.get(w)+" ";
      }
    }

    return v;
  }

  // ACTGsort
  static String[] getACTGsort(int n) {
    String[] v = new String[n];
    for (int i = 0; i < n; i++) {
      int l = 1+(int)(Math.random() *(201));
      v[i] = "";
      for (int j = 0; j < l ; j++) {
        int DNA = (int)(Math.random() *4);
        if (DNA == 0) v[i] += "A";
        else if (DNA == 1) v[i] += "C";
        else if (DNA == 2) v[i] += "T";
        else if (DNA == 3) v[i] += "G";
      }
    }

    return v;
  }

  // 01*sort
  static String[] getbinarysort(int n) {
    String[] v = new String[n];
    for (int i = 0; i < n; i++) {
      int l = 1+(int)(Math.random() *(101));
      v[i] = "";
      for (int j = 0; j < l ; j++) {
        if ((int)(Math.random() *2) == 0) v[i] += "0";
        else v[i] += "1";
      }
    }

    return v;
  }

  // 01sort
  static int[] getbitsort(int n) {
    int[] v = new int[n];
    for (int i = 0; i < n; i++)
      v[i] = (int)(Math.random() *2);

    return v;
  }

  // ~sort
  static int[] getSimilarsort(int n) {
    int[] v = new int[n];
    for (int i = 0; i < n; i++)
      v[i] = (int)(Math.random() *(Math.max(2,Math.log(n)/Math.log(10))));

    return v;
  }

  // csort
  static int[] getcsort(int n, int c) {
    int[] v = new int[n];
    for (int i = 0; i < n; i++)
      v[i] = i; // sem elementos repetidos

    for (int i = 0; i < n-c; i += c) {
      for (int j = 0; j < c; j++) {
        int pos = i+ (int)(Math.random() *(j+1)); //sorteia de [i,i+j]
        int tmp = v[pos]; // troca
        v[pos] = v[i+j];
        v[i+j] = tmp;
      }
    }

    return v;
  }

  //+sort
  static double[] getPlussort(int n) {
    double v[] = new double[n];
    for (int i =0; i <n-10; i++)
      v[i]=i;
    for (int i=n-10; i < n; i++)
      v[i] = Math.random();

    return v;
  }

  // %sort
  static int[] getPercentsort(int n) {
    int[] v = new int[n];
    for (int i = 0; i < n; i++)
      v[i] = i; // sem elementos repetidos

    for (int i = 0; i < n/100; i++) {
      int pos = (int)(Math.random() *(n)); //sorteia de [0,n-1]
      v[pos] = (int)(Math.random() *(n)); // troca por numero fora de ordem
    }

    return v;
  }

  // 3sort
  static int[] get3sort(int n) {
    int[] v = new int[n];
    for (int i = 0; i < n; i++)
      v[i] = i; // sem elementos repetidos

    for (int i = 0; i < 3; i++) {
      int pos = (int)(Math.random() *(n)); //sorteia de [0,n-1]
      v[pos] = n+i; // troca por numero fora de ordem
    }

    return v;
  }
  // *sort
  static int[] getRandomPermutation(int n) {
    int[] v = new int[n];
    for (int i = 0; i < n; i++)
      v[i] = i; // sem elementos repetidos

    for (int i = 0; i < n; i++) {
      int pos = (int)(Math.random() *(i+1)); //sorteia de [0,i]
      int tmp = v[pos]; // troca
      v[pos] = v[i];
      v[i] = tmp;
    }

    return v;
  }

  public static void main(String args[]) throws Exception {
    if (args.length < 1) {
      System.err.println("Escolha um tipo de modelo");
      System.err.println("[0]*sort [1]/sort, [2]\\sort, [3]/sort, [4]\\/sort [5]/\\sort");
      System.err.println("[6]3sort, [7]+sort, [8]%sort, [9]csort, [10]=sort, [11]~sort, [12]01sort, [13]01*sort, [14]ACTGsort, [15]PTsort");
      System.exit(-1);
    }
    String modelo = args[0];
    int N = 100000;
    if (args.length >1) {
      N = Integer.valueOf(args[1]); //100000;
    }

    if (args[0].equals("*sort") || args[0].equals("0"))
      for (int x: getRandomPermutation(N)) System.out.println(x);

    if (args[0].equals("/sort")|| args[0].equals("1"))
      for (int i = 0; i < N; i++) System.out.println(i);

    if (args[0].equals("\\sort")|| args[0].equals("2"))
      for (int i = N-1; i >= 0; i--) System.out.println(i);

    if (args[0].equals("/\\sort")|| args[0].equals("3")) {
      for (int i = 0; i <= N/2; i++)      System.out.println(i);
      for (int i = N-1; i>= 1 + N/2; i--) System.out.println(i);
    }

    if (args[0].equals("\\/sort")|| args[0].equals("4")) {
      for (int i = N-1; i >= N/2; i--) System.out.println(i);
      for (int i = 0; i < N/2; i++)    System.out.println(i);
    }

    if (args[0].equals("3sort")|| args[0].equals("5"))
      for (int x: get3sort(N)) System.out.println(x);

    if (args[0].equals("+sort")|| args[0].equals("6"))
      for (double x: getPlussort(N)) System.out.println(x);

    if (args[0].equals("%sort")|| args[0].equals("7"))
      for (int x: getPercentsort(N)) System.out.println(x);

    if (args[0].equals("csort")|| args[0].equals("8"))
      for (int x: getcsort(N, (int)Math.sqrt(N))) System.out.println(x);

    if (args[0].equals("=sort")|| args[0].equals("9"))
      for (int i =0; i < N; i++) System.out.println("0");

    if (args[0].equals("~sort")|| args[0].equals("10"))
      for (int x: getSimilarsort(N)) System.out.println(x);

    if (args[0].equals("01sort")|| args[0].equals("11"))
      for (int x: getbitsort(N)) System.out.println(x);

    if (args[0].equals("01*sort")|| args[0].equals("12"))
      for (String x: getbinarysort(N)) System.out.println(x);

    if (args[0].equals("ACTGsort")|| args[0].equals("13"))
      for (String x: getACTGsort(N)) System.out.println(x);

    if (args[0].equals("PTsort")|| args[0].equals("14"))
      for (String x:getPTsort(N)) System.out.println(x);

  }

}
