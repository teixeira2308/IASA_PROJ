from lib.pee.melhor_prim.ProcuraMelhorPrim import ProcuraMelhorPrim
from lib.pee.melhor_prim.aval.AvaliadorCustoUnif import AvaliadorCustoUnif

"""
    Esta classe representa a ProcuraCustoUnif, que é uma classe para implementar
    o algoritmo de procura de custo uniforme. Ela herda da classe ProcuraMelhorPrim.
    O objetivo do algoritmo de procura de custo uniforme é encontrar o caminho de menor custo
    entre o nó inicial e o nó objetivo, considerando o custo acumulado para chegar a cada
    nó. Ele é uma variação do algoritmo de procura do melhor primeiro, onde a avaliação dos nós
    é feita com base no custo acumulado para chegar a cada nó, em vez de uma estimativa do custo para chegar ao objetivo. 
"""

class ProcuraCustoUnif(ProcuraMelhorPrim):
    def __init__(self):
        super().__init__(AvaliadorCustoUnif()) # retorna a classe AvaliadorCustoUnif, que é a classe responsável
                                               #por atribuir a prioridade a cada nó com base no custo acumulado para chegar a cada nó