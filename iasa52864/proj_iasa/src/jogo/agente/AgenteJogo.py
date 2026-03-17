from abc import ABC, abstractmethod

"""
    Atua como o controlador do topo do sistema. É a classe responsável por instanciar o AmbienteJogo e o Agente.
    Garante que o ciclo de vida do programa seja mantido.
"""

from lib.agente.Agente import Agente
from jogo.agente.PercepcaoJogo import PercepcaoJogo

class AgenteJogo(Agente):
    def __init__(self, ambiente, controlo):
        super().__init__(controlo)
        self._ambiente = ambiente

    def _percecionar(self):
        """ Obter as perceções do ambiente. """
        return PercepcaoJogo(self._ambiente.observar())

    def actuar(self, accao):
        """ Executar passo de pensamento """
        if accao is not None:
            self._ambiente.executar(accao)
