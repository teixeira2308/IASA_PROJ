"""
    Avaliador de custo uniforme, é uma classe que implementa a avaliação dos nós com base no custo acumulado para chegar a cada nó.
"""

class AvaliadorCustoUnif:
    def prioridade(self, no):
        #f(n) = g(n)
        return no.custo #retorna o custo acumulado para chegar a cada nó
    
