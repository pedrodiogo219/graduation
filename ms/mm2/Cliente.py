class Cliente:
    def __init__(self, t_chegada, t_servico):
        self.t_chegada = t_chegada
        self.t_servico = t_servico

    def __repr__(self):
        return "tempo de chegada:" + str(self.t_chegada) + "\ntempo necessario para atendimento:" + str(self.t_servico)
