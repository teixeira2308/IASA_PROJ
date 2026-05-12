from lib.mod.Problema import Problema

class ProblemaPlan(Problema):
    """
        Representa a formulação de um problema de planemaneto para ser resolvido 
        por um motor de procura. Define o estado inicial, os operadores disponíveis
        e a condição de objetivo.
    """
    def __init__(self, modelo_plan, estado_final):
        """
            Construtor do problema de planeamento.

            Parâmetros:
                modelo_plan: O modelo que fornece o estado atual e os operadores.
                estado_final: O estado (posição) que o agente deseja atingir.
        """
        self.__estado_final = estado_final
        # Invoca o construtor da superclasse Problema
        # definindo o ponto de partida e o conjunto de ações possíveis
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())

    def objetivo(self, estado):
        """
            Critério de paragem da procura.
            Verifica se um estado gerado durante a exploração é igual
            ao estado final pretendido.
        """
        return estado == self.__estado_final