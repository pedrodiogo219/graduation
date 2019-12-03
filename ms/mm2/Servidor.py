class Servidor:
    def __init__(self):
        self.ocupado = False
        self.tempoFimAtendimentoAtual = 0

    def atende(self, cliente):
        self.ocupado = True
        self.tempoFimAtendimentoAtual = cliente.t_atendimento + cliente.t_servico

    def libera(self):
        self.ocupado = False
