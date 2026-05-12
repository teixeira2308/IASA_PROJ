from lib.pee.melhor_prim.Heuristica import Heuristica
import math

class HeurDist(Heuristica):

    """
        Implementação da heurística baseada na Distância.
        Fornece uma estimativa do custo restante desde o 
        estado atual até ao estado objetivo.
    """

    def __init__(self, estado_final):
        """
            Inicializa a heurística com o estado objetivo para o
            cálculo da distância
        """
        self.__estado_final = estado_final

    def h(self, estado):
        """
            Calcula a distância em linha reta entre o estado atual
            e o estado final.
        """
        return math.dist(self.__estado_final, estado)