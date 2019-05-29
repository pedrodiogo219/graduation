from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def printa_dados(dados):
    for n, tempos in dados.items():
        print(n)
        print(tempos)


def plota(dados):
    y = []
    x = []
    y2 = []

    for n, array in dados.items():
        x.append(n)
        media = array.mean()
        y.append(media)
        y2.append(razao)

    print(x)
    print(y)
    plt.plot(x, y)


def main():

    dados = {}

    try:
        while True:
            n = input()
            n = int(n)
            tempo = input()

            s = ""
            for l in tempo:
                if l == ',':
                    s +='.'
                else:
                    s += l

            s=float(s)
            if n not in dados:
                dados[n] = np.array([])
            dados[n] = np.append(dados[n], s)

    except Exception as e:
        #printa_dados(dados)
        plota(dados)




main()
