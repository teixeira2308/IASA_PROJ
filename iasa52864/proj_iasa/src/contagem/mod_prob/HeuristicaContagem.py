"""
Heurística de contagem para o problema da contagem.
A heurística é uma função que estima o custo de chegar ao estado objetivo a partir do estado atual.
No caso do problema da contagem, a heurística é a diferença absoluta entre a contagem atual e a contagem final.
"""

class HeuristicaContagem:
    def __init__(self, contagem_final):
        self.__contagem_final = contagem_final #valor de contagem final, que é o estado objetivo do problema.

    def h(self, estado):
        return abs(self.__contagem_final - estado.contagem) 
    """
        A função heurística h recebe um estado e retorna a diferença absoluta (módulo) entre a contagem final e a contagem do estado.
    """