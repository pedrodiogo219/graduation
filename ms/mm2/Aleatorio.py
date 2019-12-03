import math

class Aleatorio:
    def __init__(self, seed=42, a=1103515245, b=12345, m=2 ** 31):
        self.anterior = seed
        self.a = a
        self.b = b
        self.m = m

    def gera_num_aleatorio(self):
        num_aleatorio = (self.a * self.anterior + self.b) % self.m
        self.anterior = num_aleatorio

        return num_aleatorio / float(self.m)

    def exponencial(self, lbd=1):
        exp = (-1) * (1 / lbd) * math.log(1 - self.gera_num_aleatorio())

        return exp

    def normal(self, mu=0, sigma=1):
        r1 = self.gera_num_aleatorio()
        r2 = self.gera_num_aleatorio()

        z1 = math.cos(2 * math.pi * r2) * math.sqrt((-2) * math.log(r1))
        z2 = math.sin(2 * math.pi * r2) * math.sqrt((-2) * math.log(r1))

        z1 = sigma * z1 + mu
        z2 = sigma * z2 + mu

        if r1 > r2:
            return z1
        return z2