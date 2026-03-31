from lib.ecr.Estimulo import Estimulo

class EstimuloObst(Estimulo):
    INTENS_OBST = 1

    def detetar(self, percecao):
        return self.INTENS_OBST if percecao.contacto_obst() else 0
