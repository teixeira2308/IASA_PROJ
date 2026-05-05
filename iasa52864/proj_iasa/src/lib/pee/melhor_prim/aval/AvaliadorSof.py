from lib.pee.melhor_prim.aval.AvaliadorHeur import AvaliadorHeur

"""
    Esta classe representa o AvaliadorSof, que é uma classe para implementar o mecanismo de procura Sofrega (Greedy Best-First Search).
    O AvaliadorSof é responsável por atribuir uma prioridade a cada nó, utilizando a função de avaliação f(n) = h(n), onde
    h(n) é a heurística que estima o custo de chegar ao estado objetivo a partir do estado do nó n.
    O mecanismo de procura Sofrega seleciona o nó com a menor heurística, ou seja, o nó que parece estar mais próximo do objetivo,
    sem considerar o custo acumulado para chegar a esse nó.
"""

class AvaliadorSof(AvaliadorHeur):
    def prioridade(self, no):
        #f(n) = h(n)
        return self.heuristica.h(no.estado) #retorna a heurística do nó, ou seja, a estimativa do custo para chegar ao objetivo a partir do nó atual