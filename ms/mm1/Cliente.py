class Cliente:
    def __init__(self, t_chegada, t_servico):
        self.t_chegada = t_chegada
        self.t_servico = t_servico

    def __repr__(self):
        return "Cliente t_cheg=" + str(self.t_chegada) + " t_serv=" + str(self.t_servico)
