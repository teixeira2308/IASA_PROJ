from lib.pee.mec_proc.ProcuraGrafo import ProcuraGrafo
from lib.pee.melhor_prim.aval.Avaliador import Avaliador

"""
Classe que implementa a procura do melhor primeiro.
Responsável por implementar o algoritmo de procura do melhor primeiro, que é uma estratégia de procura.
"""

class ProcuraMelhorPrim(ProcuraGrafo):
    def __init__(self, avaliador):
        super().__init__(avaliador) #chama o construtor da classe pai passando uma instância de Avaliador, que é 
                                    #a estrutura de dados utilizada para avaliar os nós a serem explorados.
        self.__avaliador = avaliador 

    def _manter(self, no):
        return super()._manter(no) or no.custo < self._explorados[no.estado].custo 
        #chama o método _manter da classe pai para verificar se o nó deve ser mantido na fronteira ou não,
        #ou se o custo do nó é menor do que o custo do nó já explorado com o mesmo estado. Se o nó deve ser mantido na
        #fronteira ou se o custo do nó é menor do que o custo do nó já explorado com o mesmo estado, então o nó
        #deve ser mantido na fronteira, caso contrário, ele deve ser descartado.