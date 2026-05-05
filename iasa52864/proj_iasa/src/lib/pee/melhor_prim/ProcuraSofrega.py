from lib.pee.melhor_prim.ProcuraMelhorPrim import ProcuraMelhorPrim
from lib.pee.melhor_prim.aval.AvaliadorSof import AvaliadorSof

"""
    Esta classe representa a ProcuraSofrega, que é uma classe para implementar o mecanismo de procura Sofrega.
    O ProcuraSofrega é uma implementação do algoritmo de busca informada, que utiliza uma função de avaliação para atribuir
    uma prioridade a cada nó, guiando a busca em direção ao objetivo. Ele é uma variação do algoritmo de procura do melhor primeiro,
    onde a avaliação dos nós é feita com base na heurística que estima o custo para chegar ao objetivo a partir de cada nó,
    sem considerar o custo acumulado para chegar a esse nó.
"""

class ProcuraSofrega(ProcuraMelhorPrim):
    def __init__(self):
        return super().__init__(AvaliadorSof())