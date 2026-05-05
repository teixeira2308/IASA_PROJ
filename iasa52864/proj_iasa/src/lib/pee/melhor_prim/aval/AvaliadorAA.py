from lib.pee.melhor_prim.aval.AvaliadorHeur import AvaliadorHeur

"""
    Esta classe representa o AvaliadorAA, que é uma classe para implementar o mecanismo de procura AA (A* Admissível). 
    O AvaliadorAA é responsável por atribuir uma prioridade a cada nó, utilizando a função de avaliação f(n) = g(n) + h(n), onde
    g(n) é o custo acumulado para chegar ao nó n a partir do nó inicial, e h(n) é a heurística que estima o custo de chegar ao estado
    objetivo a partir do estado do nó n.
    
"""

class AvaliadorAA(AvaliadorHeur):
    def prioridade(self, no):
        #f(n) = g(n) + h(n)
        return no.custo + self.heuristica.h(no.estado) #retorna o custo acumulado para chegar a cada nó + a heurística do nó