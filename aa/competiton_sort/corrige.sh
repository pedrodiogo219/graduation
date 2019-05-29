rm -rf tempos.txt
TIMEFORMAT="%3R"
i=0
while [ $i -le $2 ];
do
  {
    j=1
    while [ $j -le $3 ] ;
    do
      {
        echo -e $i >> tempos.txt;
        java Generator $1 $i > entrada.txt;
        { time ./stooge < entrada.txt > saida.txt; } 2>> tempos.txt
        sort -g entrada.txt > correto.txt
        diff saida.txt correto.txt
        let j=j+1;
      }
    done;
    let i=i+100;
  }
done
