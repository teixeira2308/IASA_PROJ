from lib.pee.melhor_prim.ProcuraInformada import ProcuraInformada
from lib.pee.melhor_prim.aval.AvaliadorAA import AvaliadorAA

"""
    Esta classe representa o ProcuraAA, que é uma classe para implementar o mecanismo de procura AA (A* Admissível).
    O ProcuraAA é uma implementação do algoritmo A* (A-star), que é um algoritmo de busca informada que utiliza uma
    função de avaliação f(n) = g(n) + h(n), onde g(n) é o custo acumulado para chegar ao nó n a partir do nó inicial,
    e h(n) é a heurística que estima o custo de chegar ao estado objetivo a partir do estado do nó n.
"""

class ProcuraAA(ProcuraInformada):
    def __init__(self):
        return super().__init__(AvaliadorAA()) # retorna a classe AvaliadorAA, que é a classe responsável
                                               #por atribuir a prioridade a cada nó com base na função de avaliação f(n) = g(n) + h(n)