from lib.ecr.Estimulo import Estimulo

'''
    A classe EstimuloObst representa o estímulo de detetar um obstáculo.

    Este estimulo é ativado quando o agente deteta a presença de um obstáculo,
    e a sua intensidade é fixa (INTENS_OBST), indicando a necessidade de evitar 
    o obstáculo.
'''

class EstimuloObst(Estimulo):
    INTENS_OBST = 1

    def detetar(self, percecao):
        return self.INTENS_OBST if percecao.contacto_obst() else 0
