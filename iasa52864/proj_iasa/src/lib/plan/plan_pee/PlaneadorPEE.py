from lib.plan.Planeador import Planeador
from lib.pee.melhor_prim.ProcuraAA import ProcuraAA
from contagem.mod_prob.ProblemaPlan import ProblemaPlan
from contagem.mod_prob.HeurDist import HeurDist
from lib.plan.plan_pee.PlanoPEE import PlanoPEE

class PlaneadorPEE(Planeador):
    """
        Componente de planeamento baseado em Procura em Espaço de Estados (PEE).
        Utiliza o algoritmo A* para encontrar o camminho otimizado entre o estado
        atual do agente e o objetivo definido.
    """
    def __init__(self):
        # Motor de procura informada A*
        self.__mec_pee = ProcuraAA()

    def planear(self, modelo_pan, objetivos):
        """
            Gera um plano de ação para atingir o primeiro objetivo da lista.

            Parâmetros:
                modelo_pan: Modelo do mundo para extração do estado inicial e operadores.
                objetivos: Lista de estados objetivo (neste caso, foca-se no primeiro).
        """

        # Define o objetivo atual (ponto de chegada)
        objetivo = objetivos[0]
        # Formulação do problema de procura com base no modelo e objetivo
        problema = ProblemaPlan(modelo_pan, objetivo)
        # Instanciação da heurística de distância para guiar o A*
        heuristica = HeurDist(objetivo)
        # Execução da procura para encontrar uma sequência de operadores (solução)
        solucao = self.__mec_pee.procurar(problema, heuristica)
        # Se for encontrada uma solução, encapsula-a num objetivo Plano
        if solucao:
            return PlanoPEE(solucao)
        return None
        