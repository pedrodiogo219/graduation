from numpy import random, round
from queue import Queue
import configparser
import os
from Cliente import Cliente
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
        self.config = self.config['MM1']


    def gera_entradas(self):

        tMedioEntreChegadas = float(self.config['tMedioEntreChegadas'])
        tMedioAtendimento = float(self.config['tMedioAtendimento'])

        if self.config['distTEC'] == 'exponencial':
            distTEC = list(map(round, r.exponential(tMedioEntreChegadas, size=10000)))
        elif self.config['distTEC'] == 'normal':
            distTEC = list(map(round, r.normal(tMedioEntreChegadas, size=10000)))
        else:
            distTEC = [tMedioEntreChegadas for _ in range(10000)]

        if self.config['distServico'] == 'exponencial':
            distServico = list(map(round, r.exponential(tMedioAtendimento, size=10000)))
        elif self.config['distServico'] == 'normal':
            distServico = list(map(round, r.normal(tMedioAtendimento, size=10000)))
        else:
            distServico = [tMedioAtendimento for _ in range(100000)]



        tempoAtual = 0
        self.clientes = []
        self.clientes.append(Cliente(0, distServico.pop(0)))
        while tempoAtual + distTEC[0] <= int( self.config['tTotaldeSimulacao'] ):
            tempoAtual += distTEC.pop(0)
            novoCliente = Cliente( int(tempoAtual), int(distServico.pop(0)) )
            self.clientes.append(novoCliente)


    def processa(self):
        tempoAtual = 0
        tempoOcioso = 0
        i = 0
        for c in self.clientes:
            if tempoAtual < c.t_chegada:
                print(f"sistema espera por {c.t_chegada - tempoAtual} minutos\n")
                tempoOcioso+= c.t_chegada - tempoAtual
                tempoAtual = c.t_chegada
            c.t_fila = tempoAtual - c.t_chegada
            c.t_atendimento = tempoAtual
            c.t_noSistema = c.t_atendimento+c.t_servico-c.t_chegada
            tempoAtual+= c.t_servico

            i+=1
            print(f"Cliente num.{i}")
            print(c)
            print(f"tempoAtendimento: {c.t_atendimento}")
            print(f"tempoSaida: {c.t_atendimento+c.t_servico}")
            print(f"tempo no sistema: {c.t_noSistema}\n")

        print(f"Tempo ocioso do sistema: {tempoOcioso}")
        print(f"Tempo medio no sistema por cliente: { mean([c.t_noSistema for c in self.clientes])}")
        print(f"Tempo medio na fila por cliente: { mean([c.t_fila for c in self.clientes])}")
        print(f"Tempo medio de servico por cliente: {mean([c.t_servico for c in self.clientes])}")


def main():
    Fila()


if __name__ == "__main__":
    main()
