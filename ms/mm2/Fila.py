from numpy import random, round
from queue import Queue
import configparser
import os
from Cliente import Cliente
from Aleatorio import Aleatorio
from Servidor import Servidor
import numpy.random as r
from statistics import mean


class Fila:
    def __init__(self):
        folder = "/".join( os.path.realpath(__file__).split('/')[:-1] )
        self.configure( folder + '/configs.env' )
        self.gera_entradas()
        self.processa()


    def configure(self, configFilename):
        self.config = configparser.ConfigParser()
        self.config.read(configFilename)
        self.config = self.config['MM2']


    def gera_entradas(self):

        variaveisAleatorias = Aleatorio(seed=float(self.config['seed']))

        tMedioEntreChegadas = float(self.config['tMedioEntreChegadas'])
        tMedioAtendimento = float(self.config['tMedioAtendimento'])

        if self.config['distTEC'] == 'exponencial':
            distTEC = [variaveisAleatorias.exponencial(1 / tMedioEntreChegadas) for _ in range(10000)]
        elif self.config['distTEC'] == 'normal':
            distTEC = [variaveisAleatorias.normal(tMedioEntreChegadas) for _ in range(10000)]
        else:
            distTEC = [tMedioEntreChegadas for _ in range(10000)]

        if self.config['distServico'] == 'exponencial':
            distServico = [variaveisAleatorias.exponencial(1 / tMedioAtendimento) for _ in range(10000)]
        elif self.config['distServico'] == 'normal':
            distServico = [variaveisAleatorias.normal(tMedioAtendimento) for _ in range(10000)]
        else:
            distServico = [tMedioAtendimento for _ in range(100000)]



        tempoAtual = 0
        self.clientes = []
        self.clientes.append(Cliente(0, int(distServico.pop(0))))
        while tempoAtual + distTEC[0] <= int( self.config['tTotaldeSimulacao'] ):
            tempoAtual += distTEC.pop(0)
            novoCliente = Cliente( int(tempoAtual), int(distServico.pop(0)) )
            self.clientes.append(novoCliente)


    def processa(self):
        tempoAtual = 0
        tempoOcioso = 0
        i = 0

        serv1 = Servidor()
        serv2 = Servidor()

        for c in self.clientes:
            i+=1
            print(f"Cliente num.{i}")
            print(c)

            if tempoAtual == serv1.tempoFimAtendimentoAtual:
                serv1.libera()
            if tempoAtual == serv2.tempoFimAtendimentoAtual:
                serv2.libera()

            if tempoAtual < c.t_chegada:
                if not serv1.ocupado:
                    print(f"servidor 1 ficou ocioso por {c.t_chegada - tempoAtual} minutos")
                if not serv2.ocupado:
                    print(f"servidor 2 ficou ocioso por {c.t_chegada - tempoAtual} minutos")
                tempoOcioso+= c.t_chegada - tempoAtual
                tempoAtual = c.t_chegada

            if not serv1.ocupado:
                c.t_fila = tempoAtual - c.t_chegada
                c.t_atendimento = tempoAtual
                c.t_noSistema = c.t_atendimento+c.t_servico-c.t_chegada
                print("servidor 1 atende o cliente")
                serv1.atende(c)

            elif not serv2.ocupado:
                c.t_fila = tempoAtual - c.t_chegada
                c.t_atendimento = tempoAtual
                c.t_noSistema = c.t_atendimento+c.t_servico-c.t_chegada
                print("servidor 2 atende o cliente")
                serv2.atende(c)

            tempoAtual = min(serv1.tempoFimAtendimentoAtual, serv2.tempoFimAtendimentoAtual)


            print(f"tempo de inicio do atendimento: {c.t_atendimento}")
            print(f"tempo de saida: {c.t_atendimento+c.t_servico}")
            print(f"tempo no sistema: {c.t_noSistema}\n")

        print(f"Tempo medio de ociosidade por servidor: {tempoOcioso/2.0}")
        print(f"Tempo medio no sistema por cliente: { mean([c.t_noSistema for c in self.clientes])}")
        print(f"Tempo medio na fila por cliente: { mean([c.t_fila for c in self.clientes])}")
        print(f"Tempo medio de servico por cliente: {mean([c.t_servico for c in self.clientes])}")


def main():
    Fila()


if __name__ == "__main__":
    main()
